# airflow-ingestion

This repo contains Airflow DAGs for loading CSV data into Snowflake staging.

## Prerequisites

- Airflow ≥ 2.x with the Amazon and Snowflake providers installed  
- Airflow connections:  
  - `aws_default` for S3 (if/when you add S3 ingestion)  
  - `snowflake_default` for Snowflake  
- An Airflow Variable `csv_local_path` pointing to your test CSV file

## First DAG: `local_csv_to_snowflake`

1. Stage a local file into a Snowflake internal stage via `snowsql PUT`.  
2. Copy it into a staging table with `COPY INTO`.  

### To deploy

```bash
pip install -r requirements.txt
airflow db init
airflow webserver --port 8080
airflow scheduler
```


## Progress

- **Week 1 (2025-05-05):** Scaffolding repo and implemented `local_csv_to_snowflake` DAG to stage a local CSV into Snowflake.
