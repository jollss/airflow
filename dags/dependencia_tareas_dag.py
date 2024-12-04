from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator
from datetime import datetime

def print_hello():
    return print('hello world with python in airflow')

with DAG(dag_id='dependencias',
         description='DAG con dependencias',
         schedule_interval='@once',
         start_date=datetime(2022, 7, 1)) as dag:

    t1 = PythonOperator(task_id='t1_primer_task_python',
                        python_callable=print_hello)

    t2 = BashOperator(task_id='t2_task_bash',
                      bash_command='echo "Tarea 2"')

    t3 = BashOperator(task_id='t3_task_bash', bash_command='echo "Tarea 3"')

    t4 = BashOperator(task_id='t4_task_bash', bash_command='echo "Tarea 4"')

    t1.set_downstream([t2, t3])
    [t2, t3] >> t4