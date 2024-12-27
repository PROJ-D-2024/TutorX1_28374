from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import pandas as pd


def download_data(**kwargs):
    print("Downloading data...")
    df = pd.read_csv('../data/dataset.csv')
    print("Data successfully read from /data/dataset.csv")


def split_and_upload_data(**kwargs):
    print("Splitting data...")
    df = pd.read_csv('../data/dataset.csv')
    train = df.sample(frac=0.8, random_state=42)
    test = df.drop(train.index)

    train.to_csv('../data/training_data.csv', index=False)
    test.to_csv('../data/fine_tuning_data.csv', index=False)
    print("Training and Fine-tuning datasets saved to /data/")


default_args = {
    'owner': 'airflow',
    'retries': 1,
}

with DAG(
    'dag1_download_split',
    default_args=default_args,
    start_date=datetime(2023, 1, 1),
    schedule_interval=None,
) as dag:
    download_task = PythonOperator(
        task_id='download_data',
        python_callable=download_data,
    )

    split_upload_task = PythonOperator(
        task_id='split_and_upload_data',
        python_callable=split_and_upload_data,
    )

    download_task >> split_upload_task
