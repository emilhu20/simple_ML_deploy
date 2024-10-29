import pandas as pd
import numpy as np

"""
Script to load the dataset from a csv file
"""
def get_csv_data(path):
    # Load the dataset
    data = pd.read_csv(path)
    data = data.replace(np.nan, None, regex=True)

    return data


