from airflow import DAG
from airflow.operators.python import PythonOperator

from datetime import datetime


def print_hello():
    print('Hola haciendo print desde python operator')

with DAG(
    dag_id='python_operator',
    description='Fisrt dag using python operator',
    schedule_interval='@once',
    start_date=datetime(2022,8,1)
    ) as dag:
    
    t1 = PythonOperator(
        task_id = 'hello_with_python',
        python_callable = print_hello
    )