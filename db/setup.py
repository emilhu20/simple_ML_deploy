
import mysql.connector
from config import DB_CONFIG, data_path
from db.connection import create_connection
from utils.data_loading import get_csv_data
from db.queries import insert_query


#------------SETUP DATABASE AND TABLE----------------
def create_database(db_name=DB_CONFIG['database']):
    """
    Create a database with the name specified in the config file.
    """
    connection = mysql.connector.connect(
        host=DB_CONFIG['host'],          # e.g., 'localhost'
        user=DB_CONFIG['user'],          # your MySQL username
        password=DB_CONFIG['password'],  # your MySQL password
    )

    cursor = connection.cursor()

    try:
        # Execute the CREATE DATABASE SQL statement
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {db_name}")
        print(f"Database '{db_name}' created successfully.")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()
        connection.close()


def create_table(sql_file_path):
    """
    Create a table in the database with the name specified in the config file.
    """
    #create a connection
    connection = create_connection()
    cursor = connection.cursor()

    # Read the SQL file
    with open(sql_file_path, 'r') as file:
        table_query = file.read()

    # Execute the table creation command
    try:
        cursor.execute(table_query)
        connection.commit()
        print("Table created successfully.")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()
        connection.close()

"""
if __name__ == "__main__":
    #create database and tables
    create_database()
    create_table("../sql/persons_table.sql")

    #load data
    data = get_csv_data(data_path)

    #insert data into the table
    #read the sql file and insert the data
    insert_query("sql/insert_csv_file_manual.sql", data)


"""