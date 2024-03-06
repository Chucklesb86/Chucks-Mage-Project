import pyarrow as pa
import pyarrow.parquet as pq
import pandas as pd
from pandas import DataFrame
import os

if 'data_exporter' not in globals():
    from mage_ai.data_preparation.decorators import data_exporter

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = "/home/src/clean-circle-414817-83009c4c2c89.json"
bucket_name = 'mage-zoomcamp-chuck'
project_id = 'clean-circle-414817'
table_name = "nyc_green_taxi_data"
object_key = 'nyc_green_taxi_data.parquet'
root_path = f'{bucket_name}/{table_name}'

@data_exporter
def export_data_to_google_cloud_storage(df: DataFrame, **kwargs) -> None:
    # creating a new date column from the existing datetime column
    df['lpep_pickup_date'] = pd.to_datetime(df['lpep_pickup_datetime'], errors='coerce').dt.date

    table = pa.Table.from_pandas(df)

    gcs = pa.fs.GcsFileSystem()

    pq.write_to_dataset(
        table,
        root_path=root_path,
        partition_cols=['lpep_pickup_date'],
        filesystem=gcs
    )
