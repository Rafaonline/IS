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

        finally:
            if self.connection:
                self.cursor.close()
                self.connection.close()


# Assuming you have the XML content and file name ready
with open("/data/retail.xml", "r", encoding="utf-8") as file:
    xml = file.read()
file_name = "retail5.xml"

# Create an instance of the DatabaseConnection class
db_connection = DatabaseConnection()

try:
    # Insert XML document into the database
    db_connection.insert_xml_document(file_name, xml)
except Exception as error:
    print("Failed to insert data", error)
