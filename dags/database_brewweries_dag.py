from airflow.sdk import DAG
from airflow.providers.postgres.hooks.postgres import PostgresHook
import constants as cst

with DAG(
    dag_id="breweries_database_setup",
    catchup=False,
    schedule=None,
    tags=["postgres", "setup", "breweries"],
) as dag:
    # 4. Uso do PostgresOperator
    hook = PostgresHook(postgres_conn_id=cst.postgres_conn_id)
    sql_command = cst.sql_create
    hook.run(sql_command)
