import psycopg2
from psycopg2 import DatabaseError
from decouple import config


def get_connection():
    try:
        connection = psycopg2.connect(
            host="127.0.0.1",
            user="postgres",
            password="301218",
            database="postgres",
            port=5432,
        )
        connection.set_client_encoding("UTF8")  # O 'LATIN1' si es necesario
        return connection
    except DatabaseError as ex:
        print(f"DatabaseError: {ex}")
        raise
    except Exception as ex:
        print(f"Error inesperado: {ex}")
        raise
