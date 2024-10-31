"""
Configuration for the database connection.
"""
DB_CONFIG = {
    'host': 'localhost',
    'user': 'root',
    'password': 'hejgrimmeko',
    'database': 'strokes_data'
}

data_path = "../simple_ML_deploy/Data/healthcare-dataset-stroke-data.csv"


CLOUD_CONFIG = {
    'project_id': 'simplemldeploy',
    'dataset': 'stroke_data',
    'table': 'persons'
}
