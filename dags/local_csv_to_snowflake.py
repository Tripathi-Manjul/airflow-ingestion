from datetime import datetime
from airflow import DAG
from airflow.providers.snowflake.operators.snowflake import SnowflakeOperator
from airflow.operators.bash import BashOperator

default_args = {'owner': 'data-engineer'}

with DAG(
    dag_id='local_csv_to_snowflake',
    default_args=default_args,
    start_date=datetime(2025, 5, 6),
    schedule_interval=None,
    catchup=False,
) as dag:

    # 1. Copy local file to a Snowflake stage
    stage_csv = BashOperator(
        task_id='stage_csv',
        bash_command=(
            'snowsql -c snowflake_default '
            '-q "PUT file://{{ var.value.csv_local_path }} '
            '@%my_table AUTO_COMPRESS=TRUE;"'
        )
    )

    # 2. Load from stage into staging table
    load_to_staging = SnowflakeOperator(
        task_id='load_to_staging',
        snowflake_conn_id='snowflake_default',
        sql="""
        COPY INTO my_schema.my_staging_table
        FROM @%my_table
        FILE_FORMAT = (TYPE = 'CSV' SKIP_HEADER = 1);
        """
    )

    stage_csv >> load_to_staging
