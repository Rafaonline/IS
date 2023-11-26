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

    def insert_xml_document(self, file_name, xml):
        try:
            self.cursor.execute(
                "INSERT INTO imported_documents (file_name, xml) VALUES (%s, %s)",
                (file_name, xml)
            )
            self.connection.commit()
            print("Document inserted successfully!")
        except Exception as exception:
            print("Error inserting document: ", exception)

    def soft_delete_xml_document(self, file_name):
        try:
            self.cursor.execute(
                "UPDATE imported_documents SET is_deleted = True WHERE file_name = %s",
                (file_name,)
            )
            self.connection.commit()
            print("Document deleted successfully!")
        except Exception as exception:
            print("Error deleting document: ", exception)

    def close_connection(self):
        if self.connection:
            self.cursor.close()
            self.connection.close()

