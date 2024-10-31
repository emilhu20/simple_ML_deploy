import pandas as pd
import numpy as np
from google.cloud import bigquery


"""
Script to load the dataset from a csv file
"""
def get_csv_data(path):
    # Load the dataset
    data = pd.read_csv(path)
    data = data.replace(np.nan, None, regex=True)

    return data


def load_data_from_bigquery(project_id, dataset, table):
    """
    Load data from a BigQuery table into a Pandas DataFrame.

    Parameters:
    - project_id (str): Google Cloud project ID
    - dataset (str): BigQuery dataset name
    - table (str): BigQuery table name

    Returns:
    - pd.DataFrame: Data loaded from BigQuery
    """
    client = bigquery.Client(project=project_id)
    query = f"SELECT * FROM `{project_id}.{dataset}.{table}`"
    
    # Run the query and convert the result to a DataFrame
    df = client.query(query).to_dataframe()
    return df