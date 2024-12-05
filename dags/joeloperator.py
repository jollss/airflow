from typing import Any
from airflow.models.baseoperator import BaseOperator

class joeloperator(BaseOperator):
    
    def __init__(self, name:str, **kwargs):
        super().__init__(**kwargs)

        self.name= name

    def execute(self, context):
        # Primera funcionalidad
        self.say_hello(context)
        # Segunda funcionalidad
        self.test_function(context)
    
    def say_hello(self, context):
        print(f"Hola {self.name}")

    def test_function(self, context):
        print("___________________-test")