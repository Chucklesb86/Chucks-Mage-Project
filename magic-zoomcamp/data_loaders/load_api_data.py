import io
import pandas as pd
import glob
import os
from datetime import datetime
import requests
if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@data_loader
def load_data_from_api(*args, **kwargs):
    """
    Template for loading data from API
    """
    url_green_taxi_10 = 'https://github.com/DataTalksClub/nyc-tlc-data/releases/download/green/green_tripdata_2020-10.csv.gz'
    url_green_taxi_11 = 'https://github.com/DataTalksClub/nyc-tlc-data/releases/download/green/green_tripdata_2020-11.csv.gz'
    url_green_taxi_12 = 'https://github.com/DataTalksClub/nyc-tlc-data/releases/download/green/green_tripdata_2020-12.csv.gz'

    taxi_dtypes = {
        'Vendor_ID': 'Int64',
        'store_and_fwd_flag': 'str',
        'Rate_code_ID': 'Int64',
        'PU_Location_ID': 'Int64',
        'DO_Location_ID': 'Int64',
        'passenger_count': 'Int64',
        'trip_distance': 'float64',
        'fare_amount': 'float64',
        'extra': 'float64',
        'mta_tax': 'float64',
        'tip_amount': 'float64',
        'tolls_amount': 'float64',
        'ehail_fee': 'float64',
        'improvement_surcharge': 'float64',
        'total_amount': 'float64',
        'payment_type': 'float64',
        'trip_type': 'float64',
        'congestion_surcharge': 'float64',
    }

    parse_dates_green_taxi = ['lpep_pickup_datetime', 'lpep_dropoff_datetime']

    all_files = [url_green_taxi_10, url_green_taxi_11, url_green_taxi_12]

    return pd.concat((pd.read_csv(f) for f in all_files), ignore_index=True)


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
