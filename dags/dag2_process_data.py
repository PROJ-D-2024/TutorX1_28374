from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import pandas as pd
from sklearn.preprocessing import MinMaxScaler


def clean_data(**kwargs):
    print("Cleaning data...")
    df = pd.read_csv('../data/training_data.csv')
    df.dropna(inplace=True)
    df.drop_duplicates(inplace=True)
    df.to_csv('../data/cleaned_data.csv', index=False)
    print("Data cleaned and saved to /data/cleaned_data.csv")


def normalize_data(**kwargs):
    print("Normalizing data...")
    df = pd.read_csv('../data/cleaned_data.csv')
    scaler = MinMaxScaler()
    df[df.columns] = scaler.fit_transform(df[df.columns])
    df.to_csv('../data/normalized_data.csv', index=False)
    print("Data normalized and saved to /data/normalized_data.csv")


default_args = {
    'owner': 'airflow',
    'retries': 1,
}

with DAG(
    'dag2_process_data',
    default_args=default_args,
    start_date=datetime(2023, 1, 1),
    schedule_interval=None,
) as dag:
    clean_task = PythonOperator(
        task_id='clean_data',
        python_callable=clean_data,
    )

    normalize_task = PythonOperator(
        task_id='normalize_data',
        python_callable=normalize_data,
    )

    clean_task >> normalize_task
