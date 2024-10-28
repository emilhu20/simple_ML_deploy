import pandas as pd

"""
Script to load the dataset from a csv file
"""
def get_csv_data(path):
    # Load the dataset
    data = pd.read_csv(path)
    return data

