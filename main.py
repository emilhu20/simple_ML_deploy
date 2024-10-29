
from utils.data_loading import get_csv_data
from config import data_path
from db.queries import delete_query, fetch_query, insert_query, update_query
from db.setup import create_database, create_table



if __name__ == "__main__":
    #STEP 1: create database and tables
    #create_database()
    #create_table("sql/persons_table.sql")

    #STEP 2: load data
    #data = get_csv_data(data_path)

    #STEP 3: insert data into the table
    #read the sql file and insert the data
    #insert_query("sql/insert_csv_file_manual.sql", data)

    #STEP 4: fetch data from the table
    data = fetch_query("sql/get_all_data.sql")
    print(data)






