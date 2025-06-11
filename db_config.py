import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="0000",
        database="banking_system"
    )
print("db_config successfull.....")
