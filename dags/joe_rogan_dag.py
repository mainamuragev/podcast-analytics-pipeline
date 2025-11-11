from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import subprocess

def extract():
    subprocess.run(["python", "scripts/extract_metadata.py"], check=True)

def transform():
    subprocess.run(["python", "scripts/transform_metadata.py"], check=True)

def load():
    subprocess.run(["python", "scripts/load_to_postgres.py"], check=True)

with DAG(
    dag_id="joe_rogan_pipeline",
    start_date=datetime(2023, 1, 1),
    schedule_interval="@daily",
    catchup=False,
    tags=["youtube", "etl", "podcast"],
) as dag:

    extract_task = PythonOperator(
        task_id="extract_metadata",
        python_callable=extract
    )

    transform_task = PythonOperator(
        task_id="transform_metadata",
        python_callable=transform
    )

    load_task = PythonOperator(
        task_id="load_to_postgres",
        python_callable=load
    )

    extract_task >> transform_task >> load_task
