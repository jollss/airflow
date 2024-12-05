from airflow import DAG
from airflow.utils.trigger_rule import TriggerRule
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator, BranchPythonOperator

from datetime import datetime


def _choose(**context):

    if context['logical_date'].date() < datetime(2022, 10, 16):
        return 'task2'

    return 'task3'

with DAG(
    dag_id='09-BPO',
    description='Orquestando el dash',
    schedule_interval= '@daily',
    start_date=datetime(2022,10,1),
    end_date= datetime(2022,11,1),
    catchup=True,
    max_active_runs=1, #Los dias se ejecutan con un maximo numero de workers en paralelo
    default_args={
        'depends_on_past':True #las tardes de los dias no se ejecutan en pararelo, las ejecuciones son secuenciales y dependen de la ejecucion de la misma tarea el dia anterior
    }
        ) as dag:


    branching = BranchPythonOperator(
        task_id='Choice',
        python_callable= _choose
    )

    finish_15_10 = BashOperator(task_id='task2',
                    bash_command="sleep 2 && echo 'Task 2'"
    )

    finished_1_11 = BashOperator(task_id='task3',
                    bash_command="sleep 2 && echo 'Task 3'"
    )

    final_t = BashOperator(task_id='task4',
                    bash_command="sleep 2 && echo 'Final Part'",
                    trigger_rule = TriggerRule.NONE_FAILED
    )


    branching >> [finish_15_10, finished_1_11]

    final_t << [finish_15_10, finished_1_11]