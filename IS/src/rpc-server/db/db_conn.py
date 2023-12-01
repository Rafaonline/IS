import psycopg2


class DatabaseConnection:
    def __init__(self):
        self.connection = None
        self.cursor = None
        self.user = "is"
        self.password = "is"
        self.host = "is-db"
        self.port = "5432"
        self.database = "is"

    def connect_db(self):
        if self.connection:
            try:
                self.connection = psycopg2.connect(
                    user=self.user,
                    password=self.password,
                    host=self.host,
                    port=self.port,
                    database=self.database
                )

                self.cursor = self.connection.cursor()
                print("Connected to the Database.")

            except psycopg2.Error as e:
                print(f"Error: {e}")

    def disconnect_db(self):
        if self.connection:
            try:
                self.cursor.close()
                self.connection.close()
                print("Disconnected from the Database.")

            except psycopg2.Error as e:
                print(f"Error: {e}")

    def execute_query(self, query):
        self.connect_db()
        try:
            self.cursor.execute(query)
            result = self.cursor.fetchall()

            return result

        except Exception as e:
            return f"Error executing query: {str(e)}"

        finally:
            self.disconnect_db()

    def insert_xml_document(self, file_name, xml):
        try:
            query = f"INSERT INTO imported_documents (file_name, xml) VALUES ({file_name}, {xml})"
            self.execute_query(query)
            print("Document inserted successfully!")

        except Exception as exception:
            print("Error inserting document: ", exception)

    def soft_delete_xml_document(self, file_name):
        try:
            query = f"UPDATE imported_documents SET is_deleted = True WHERE file_name = {file_name}"
            self.execute_query(query)
            print("Document deleted successfully!")

        except Exception as exception:
            print("Error deleting document: ", exception)

