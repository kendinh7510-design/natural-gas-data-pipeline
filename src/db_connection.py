import os 
import psycopg
from dotenv import load_dotenv

load_dotenv()

def get_connection():
    conn = psycopg.connect(
        host = os.getenv("DB_HOST"),
        port = os.getenv("DB_PORT"),
        dbname = os.getenv("DB_NAME"),
        user = os.getenv("DB_USER"),
        password = os.getenv("DB_PASSWORD")
    )
    return conn

if __name__ == "__main__":
    with get_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute("SELECT current_database();")
            result = cursor.fetchone()
            print("Connected to:", result[0])