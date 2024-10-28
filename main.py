
from utils.data_processing import get_csv_data
from config import data_path
from db.queries import insert, fetch_data, update_data, delete_data
from db.setup import create_database, create_table


if __name__ == "__main__":
    #create database
    #create_database()

    #create table
    #create_table("sql/persons_table.sql")

    #load data
    data = get_csv_data(data_path)
    print(data.head())




