import psycopg2


def get_connection():
    conn = psycopg2.connect(
        host="localhost",
        port="5432",
        database="pagila",
        user="postgres",
        password="Diego2003"
    )
    return conn
