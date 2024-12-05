from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

with DAG(dag_id="5.1-orquestacion",
         description="Probando la orquestacion",
         schedule_interval="@daily",
         start_date=datetime(2024, 12, 4),
         end_date=datetime(2024, 12, 4),
         default_args={"depends_on_past": True},#cada una de las tareas depende de como se alla ejecutado de su tarea anterior
         max_active_runs=1#
         ) as dag:

    t1 = BashOperator(task_id="tarea1",
                      bash_command="sleep 3 && echo 'Tarea 1'")

    t2 = BashOperator(task_id="tarea2",
                      bash_command="sleep 4 && echo 'Tarea 2'")

    t3 = BashOperator(task_id="tarea3",
                      bash_command="sleep 5 && echo 'Tarea 3'")

    t4 = BashOperator(task_id="tarea4",
                      bash_command="sleep 6 && echo 'Tarea 4'")

    t1 >> t2 >> [t3,t4]