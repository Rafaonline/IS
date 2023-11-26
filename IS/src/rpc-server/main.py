import signal, sys
from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler

from functions.string_length import string_length
from functions.string_reverse import string_reverse
import psycopg2


class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

def search_tr_by_product(product_name):
    try:
        # Connect to the database
        connection = psycopg2.connect(user="is", password="is", host="is-db", port="5432", database="is")
        cursor = connection.cursor()

        # Execute the XML query to find Product ID based on the product name
        product_id_query = (f"SELECT xpath('//Products/Product[@name=\"{product_name}\"]/@id', xml) "
                            f"FROM public.imported_documents;")
        cursor.execute(product_id_query)
        product_id_result = cursor.fetchone()

        if not product_id_result:
            return f"Product with name '{product_name}' not found."

        product_id = product_id_result[0]

        # Execute the XML query to find transactions with the obtained Product ID
        transaction_query = (f"SELECT xpath('//Transaction[Products/Product/@id=\"{product_id}\"]/@ID', xml)"
                             f"FROM public.imported_documents;")
        cursor.execute(transaction_query)
        transaction_result = cursor.fetchall()

        # Close the database connection
        connection.close()

        return transaction_result

    except Exception as e:
        return f"Error: {str(e)}"

def execute_query(query):
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


with SimpleXMLRPCServer(('0.0.0.0', 9000), requestHandler=RequestHandler) as server:
    server.register_introspection_functions()


    def signal_handler(signum, frame):
        print("received signal")
        server.server_close()

        # perform clean up, etc. here...

        print("exiting, gracefully")
        sys.exit(0)


    # signals
    signal.signal(signal.SIGTERM, signal_handler)
    signal.signal(signal.SIGHUP, signal_handler)
    signal.signal(signal.SIGINT, signal_handler)

    # register both functions
    server.register_function(string_reverse)
    server.register_function(string_length)
    server.register_function(search_tr_by_product, 'search_tr_by_product')
    server.register_function(execute_query)

    # start the server
    print("Starting the RPC Server...")
    server.serve_forever()
