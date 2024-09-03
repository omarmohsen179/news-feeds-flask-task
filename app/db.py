import mysql.connector
from app.config import Config


def get_db_connection():
    conn = mysql.connector.connect(
        user=Config.DB_USER,
        password=Config.DB_PASSWORD,
        host=Config.DB_HOST,
        database=Config.DB_NAME,
    )
    return conn
