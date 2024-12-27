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

---

### Project Structure
