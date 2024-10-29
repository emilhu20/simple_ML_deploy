
from utils.data_processing import get_csv_data
from config import data_path
from db.queries import delete_query, fetch_query, insert_query, update_query
from db.setup import create_database, create_table



if __name__ == "__main__":
    #create database and tables
    #create_database()
    #create_table("sql/persons_table.sql")

    #load data
    data = get_csv_data(data_path)
    
    print(data.head())

    #insert data into the table
    #read the sql file and insert the data
    insert_query("sql/insert_csv_file_manual.sql", data)







