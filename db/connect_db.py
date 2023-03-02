import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()

host = os.getenv("SQL_HOST")
db_user = os.getenv("DB_USER")
password = os.getenv("PASSWORD")
db = os.getenv("DATABASE")


def create_connection():
    connection = mysql.connector.connect(
        host=host,
        user=db_user,
        password=password,
        database=db
    )
    return connection
