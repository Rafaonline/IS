import psycopg2

connection = None
cursor = None

try:
    connection = psycopg2.connect(user="is",
                                  password="is",
                                  host="is-db",
                                  port="5432",
                                  database="is")

    cursor = connection.cursor()

    cursor.execute("SELECT * FROM teachers")

    print("DOcs list:")
    for docs in cursor:
        print(f" > {docs[0]}, from {docs[1]}")

except (Exception, psycopg2.Error) as error:
    print("Failed to fetch data", error)

finally:
    if connection:
        cursor.close()
        connection.close()


