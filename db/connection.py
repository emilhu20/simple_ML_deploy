
import mysql.connector
from config import DB_CONFIG    

def create_connection():
    "Establish connection to database"
    connection = mysql.connector.connect(
        host=DB_CONFIG['host'],          # e.g., 'localhost'
        user=DB_CONFIG['user'],          # your MySQL username
        password=DB_CONFIG['password'],  # your MySQL password
        database=DB_CONFIG['database']   # the name of the database to use
    )

    return connection


