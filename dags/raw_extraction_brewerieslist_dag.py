from datetime import datetime, timedelta
import requests
import math
import json
import uuid_utils as uuid
import constants as cst

from airflow.sdk import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.trigger_dagrun import TriggerDagRunOperator

from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType, IntegerType, DoubleType
from airflow.providers.apache.spark.operators.spark_submit import SparkSubmitOperator

def raw_extraction():
    """
    Fetch data from the Open Brewery DB API and return a JSON-like dict containing both metadata and the raw payload.
    """

    lst_breweries = []

    try:
        # response_metadata = requests.get(cst.url_metadata)
        # if response_metadata.status_code == 200:
        #     total_amount = response_metadata.json()["total"]
        # else:
        #     raise requests.exceptions.HTTPError(f"Status code inválido: {response_metadata.status_code}")

        # total_page = math.ceil(total_amount / 200) + 1

        # for i in range(1, total_page):
        #     params = {"page": i, "per_page": 200}
        #     response_breweries = requests.get(cst.url_lstbreweries, params=params)

        #     if response_breweries.status_code == 200:
        #         breweries = response_breweries.json()
        #         lst_breweries.extend(breweries)
        #     else:
        #         raise requests.exceptions.HTTPError(f"Status code inválido: {response_breweries.status_code}")
        
        teste = [{
                    "id": "5128df48-79fc-4f0f-8b52-d06be54d0cec",
                    "name": "(405) Brewing Co",
                    "brewery_type": "micro",
                    "address_1": "1716 Topeka St",
                    "address_2": None,
                    "address_3": None,
                    "city": "Norman",
                    "state_province": "Oklahoma",
                    "postal_code": "73069-8224",
                    "country": "United States",
                    "longitude": -97.46818222,
                    "latitude": 35.25738891,
                    "phone": "4058160490",
                    "website_url": "http://www.405brewing.com",
                    "state": "Oklahoma",
                    "street": "1716 Topeka St"
                }]

        spark = (
                    SparkSession.builder
                    .appName("raw_breweries")
                    .master("local[*]")
                    .config("spark.jars", "/opt/airflow/jars/postgresql-42.7.3.jar")
                    .getOrCreate()
                )
        schema = StructType([
                    StructField("id", StringType(), True),
                    StructField("name", StringType(), True),
                    StructField("brewery_type", StringType(), True),
                    StructField("address_1", StringType(), True),
                    StructField("address_2", StringType(), True),
                    StructField("address_3", StringType(), True),
                    StructField("city", StringType(), True),
                    StructField("state_province", StringType(), True),
                    StructField("postal_code", StringType(), True),
                    StructField("country", StringType(), True),
                    StructField("longitude", DoubleType(), True),
                    StructField("latitude", DoubleType(), True),
                    StructField("phone", StringType(), True),
                    StructField("website_url", StringType(), True),
                    StructField("state", StringType(), True),
                    StructField("street", StringType(), True)
                ])
        df_raw = spark.createDataFrame(teste, schema=schema)
        df_raw.show(5)
        df_raw.write.jdbc(
                        url="jdbc:postgresql://postgres:5432/airflow",
                        table="bronze_breweries",
                        mode="append",
                        properties={
                            "user": "airflow",
                            "password": "airflow",
                            "driver": "org.postgresql.Driver"
                        }
                    )
        spark.stop()
        


    #     metadata_json = {
    #         "file_name": file_name,
    #         "total_amount_breweries": total_amount,
    #         "source_endpoint": f"{cst.url_lstbreweries}",
    #         "source_query": f"page={total_page}&per_page=200",
    #         "creation_timestamp": datetime.now().timestamp(),
    #         "batch_id": str(uuid.uuid7()),
    #         "bronze_target": "breweries_bronze"
    #     }

    #     with open(f"{cst.savefilepath}/{file_name}", "w", encoding="utf-8") as f:
    #         json.dump(metadata_json, f, ensure_ascii=False, indent=2)

    #     return True

    except Exception as e:

        # file_name = f"bees_listbreweries_{datetime.now().date()}.json"

        return str(e)


default_args = {"owner": "airflow", "depends_on_past": False, "email_on_failure": True, "email_on_retry": False, "retries": 1, "retry_delay": timedelta(minutes=5)}
with DAG(
    dag_id="raw_brewery_extraction",
    default_args=default_args,
    description="DAG for extract data from the Open Brewery DB API",
    schedule="@weekly", 
    start_date=datetime(2025, 11, 28),
    catchup=False,
    tags=["brewery", "raw"],
) as dag:
    raw_extract_breweries = PythonOperator(
        task_id="raw_extract_breweries",
        python_callable=raw_extraction
    )