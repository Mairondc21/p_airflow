from time import sleep
from airflow.decorators import dag,task
from datetime import datetime

@dag(
        dag_id="minha_primeira_dag",
        description="minha etl ta boa",
        schedule="* * * * *",
        start_date=datetime(2024,3,1),
        catchup=False
)
def pipeline():

    @task
    def primeira_att():
        print("Minha primeira atividade")
        sleep(2)

    @task
    def segunda_att():
        print("Minha segunda atividade")
        sleep(2)
    
    @task
    def terceira_att():
        print("Minha terceira atividade")
        sleep(2)

    @task
    def quarta_att():
        print("pipeline finalizou")

    
    t1 = primeira_att()
    t2 = segunda_att()
    t3 = terceira_att()
    t4 = quarta_att()

    #t1 >> t2 >> t3 >> t4 jeito de executar a ordem das tasks

    t1.set_downstream([t2,t3])
    t3.set_upstream(t4)

pipeline()
