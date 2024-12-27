# TutorX1_28374

# Airflow Data Processing Project

This project implements two Data Pipelines (DAGs) using Apache Airflow:

1. **DAG 1: Data Download and Splitting**
   - Downloads a dataset from a public source.
   - Splits the dataset into Training and Fine-Tuning datasets.
   - Uploads the datasets to Google Sheets.

2. **DAG 2: Data Processing**
   - Downloads the Training dataset from Google Sheets.
   - Cleans the data (handles missing values, removes duplicates).
   - Normalizes and standardizes the data.
   - Uploads the processed dataset back to Google Sheets.

### Technologies Used
- **Apache Airflow** for orchestrating workflows.
- **Pandas** and **scikit-learn** for data processing.
- **Google Sheets API** for cloud storage.

### DAGs Overview
Both DAGs are designed with modular, reusable operators and clear documentation for easy understanding and extension.

### Project Structure

project/
├── dags/
│   ├── dag1_download_split.py   # Handles data download and splitting
│   └── dag2_process_data.py     # Handles data cleaning and processing
├── requirements.txt             # Lists all Python dependencies
├── docker-compose.yaml          # Configuration for running Airflow with Docker
└── credentials.json             # Google Sheets credentials (for illustration)


### Usage

To run the project:

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
2. Start Airflow:
   docker-compose up -d
3. Access the Airflow UI:
   Open your browser and go to http://localhost:8080.
   Trigger the DAGs manually from the Airflow UI.


