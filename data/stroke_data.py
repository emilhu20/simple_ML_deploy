#!/usr/bin/python
# -*- coding: utf-8 -*-

import numpy as np  
import mysql.connector
import pandas as pd


#------------------------ FUNCTION DEFINITIONS ------------------------ 
def get_csv_data(path):
    # Load the dataset
    data = pd.read_csv(path)
    #print(data.head(3))
    return data


def insert_data(data):
    #only keep the first 7 columns
    truncated_data = data.iloc[:, 0:7]
    print(truncated_data.head(3))

    # Establish the connection to SQL database
    connection = mysql.connector.connect(
        host='localhost',          # e.g., 'localhost' or '127.0.0.1'
        user='root',              # your MySQL username
        password='hejgrimmeko',   # your MySQL password
        database='strokes_data'   # the name of the database to use
    )
    #create a cursor object using the cursor() method
    cursor = connection.cursor()

    # Strings for INSERT operation
    column_str = "id, gender, age, hypertension, heart_disease, ever_married, work_type"
    insert_str = ("%s, " * 7)[:-2]  # Corrected to 7 placeholders
    final_str = f"INSERT INTO persons ({column_str}) VALUES ({insert_str})"

    try:
        # Insert the stroke data into the database 
        data_tuples = truncated_data.values.tolist()
        cursor.executemany(final_str, data_tuples)
        connection.commit()  # Commit the transaction
  
    except mysql.connector.Error as err:
        print("Error: {}".format(err))
    finally:
        cursor.close()  # Close the cursor
        connection.close()  # Close the connection

