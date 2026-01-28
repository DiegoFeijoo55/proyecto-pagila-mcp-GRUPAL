import psycopg2
from psycopg2.extras import RealDictCursor


class Database:
    def __init__(self):
        self.config = {
            "host": "localhost",
            "port": 5432,
            "dbname": "pagila",
            "user": "postgres",
            "password": "Diego2003"
        }

    def connect(self):
        return psycopg2.connect(
            **self.config,
            cursor_factory=RealDictCursor
        )

    def execute_select(self, query, params=None):
        connection = self.connect()
        try:
            with connection.cursor() as cursor:
                cursor.execute("SET TRANSACTION READ ONLY;")
                cursor.execute(query, params)
                result = cursor.fetchall()
                return result
        finally:
            connection.close()
