# airflow-ingestion

This repo contains Airflow DAGs for loading CSV data into Snowflake staging.

## Prerequisites

- Airflow ≥ 2.x with the Amazon and Snowflake providers installed
- Airflow connections:
  - `aws_default` for S3 (if needed later)
  - `snowflake_default` for Snowflake
- A variable `csv_local_path` pointing to your test CSV

## First DAG: local_csv_to_snowflake

1. Stages a local file into a Snowflake internal stage via `snowsql PUT`.  
2. Copies it into a staging table with `COPY INTO`.

### To deploy

```bash
pip install -r requirements.txt
airflow db init
airflow webserver --port 8080
airflow scheduler
