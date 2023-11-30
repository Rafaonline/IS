import psycopg2


class DatabaseConnection:
    def __init__(self):
        self.connection = psycopg2.connect(
            user="is",
            password="is",
            host="is-db",
            port="5432",
            database="is"
        )
        self.cursor = self.connection.cursor()

    def close_connection(self):
        if self.connection:
            self.cursor.close()
            self.connection.close()

