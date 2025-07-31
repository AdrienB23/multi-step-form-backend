import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()
DB_PASSWORD = os.getenv("DB_PASSWORD")

def get_connection():
    return mysql.connector.connect(
        host='mysql-challenges.alwaysdata.net',
        user='419729',
        password=DB_PASSWORD,
        database='challenges_multi_step'
    )
