
from db.connection import create_connection
import mysql.connector
import pandas as pd



#------------------------ FUNCTION DEFINITIONS ------------------------
def insert_query(query_path, data):
    """
    Execute an insert query to insert data into the database.

    Parameters:
    query_path (str): The path to the SQL query file.
    data: The data to insert into the query.
    """
    # Convert DataFrame to a list of tuples
    data_tuples = [tuple(row) for row in data.to_numpy()]

    #create a connection to db 
    connection = create_connection()
    cursor = connection.cursor()
    

    # Read the SQL file
    with open(query_path, 'r') as file:
        query = file.read()

    try:
        cursor.executemany(query, data_tuples)
        connection.commit()
        
    except mysql.connector.Error as err:
            print(f"Error: {err}")

    finally:
            cursor.close()
            connection.close()



def fetch_query(query_path):
    """
    Execute a fetch query to retrieve data from the database.

    Parameters:
    query_path (str): The path to the SQL query file.

    Returns:
    results (list): The results of the query
    """
    #create a connection to db 
    connection = create_connection()
    cursor = connection.cursor()
    

    # Read the SQL file
    with open(query_path, 'r') as file:
        query = file.read()

    try:
        cursor.execute(query)
        results = cursor.fetchall()
        return results
        
    except mysql.connector.Error as err:
            print(f"Error: {err}")

    finally:
            cursor.close()
            connection.close()


def update_query(query_path, data):
    """
    Execute an update query to update data in the database.

    Parameters:
    query_path (str): The path to the SQL query file.
    data: The data to insert into the query.
    """
    #create a connection to db 
    connection = create_connection()
    cursor = connection.cursor()
    

    # Read the SQL file
    with open(query_path, 'r') as file:
        query = file.read()

    try:
        cursor.execute(query, data)
        connection.commit()
        
    except mysql.connector.Error as err:
            print(f"Error: {err}")

    finally:
            cursor.close()
            connection.close()


def delete_query(query_path):
    """
    Execute a delete query to delete data from the database.

    Parameters:
    query_path (str): The path to the SQL query file.
    data: The data to insert into the query.
    """
    #create a connection to db 
    connection = create_connection()
    cursor = connection.cursor()
    

    # Read the SQL file
    with open(query_path, 'r') as file:
        query = file.read()

    try:
        cursor.execute(query)
        connection.commit()
        
    except mysql.connector.Error as err:
            print(f"Error: {err}")

    finally:
            cursor.close()
            connection.close()

