import psycopg2


class Queries:

    def execute_query(self, query):
        connection = None
        cursor = None

        try:
            # Establish a database connection
            connection = psycopg2.connect(
                user="is",
                password="is",
                host="is-db",
                port="5432",
                database="is"
            )
            cursor = connection.cursor()

            # Execute the query
            cursor.execute(query)
            result = cursor.fetchall()
            connection.commit()

            return result

        except Exception as e:
            return f"Error executing query: {str(e)}"

        finally:
            if connection:
                cursor.close()
                connection.close()

    def get_tr_id_by_prod_name(self, product_name):

        product_id_query = (f"SELECT xpath('//Products/Product[@name=\"{product_name}\"]/@id', xml) "
                            f"FROM public.imported_documents;")
        product_id_result = self.execute_query(product_id_query)
        product_id = product_id_result[0]

        transaction_query = (f"SELECT xpath('//Transaction[Products/Product/@id=\"{product_id}\"]', xml) "
                             f"FROM public.imported_documents;")
        transaction_id_result = self.execute_query(transaction_query)

        return transaction_id_result

    def get_purchases(self, id_client):
        transaction_query = (
            f"SELECT xpath('//Transaction[Customer[@ID=\"{id_client}\"]]', xml) FROM public.imported_documents "
        )
        purchases_client = self.execute_query(transaction_query)
        return purchases_client
