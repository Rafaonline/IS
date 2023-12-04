import signal
import sys
from xmlrpc.server import SimpleXMLRPCRequestHandler
from xmlrpc.server import SimpleXMLRPCServer

import xmlschema

from db.db_conn import DatabaseConnection
from functions.csv_to_xml_converter import CSVtoXMLConverter
from functions.queries import Queries
from functions.string_length import string_length
from functions.string_reverse import string_reverse


class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)


with SimpleXMLRPCServer(('0.0.0.0', 9000), requestHandler=RequestHandler) as server:
    server.register_introspection_functions()
    queries = Queries()
    database = DatabaseConnection()
    converter = CSVtoXMLConverter(path='/data/Retail_Transactions_Dataset.csv')


    def signal_handler(signum, frame):
        print("received signal")
        server.server_close()

        # perform clean up, etc. here...

        print("exiting, gracefully")
        sys.exit(0)


    csv_file = '/data/Retail_Transactions_Dataset.csv'
    xsd_file = '/data/schema.xsd'
    xml_file = converter.to_xml_file()

    # xml validations
    schema = xmlschema.XMLSchema(xsd_file)
    schema.validate(xml_file)

    # signals
    signal.signal(signal.SIGTERM, signal_handler)
    signal.signal(signal.SIGHUP, signal_handler)
    signal.signal(signal.SIGINT, signal_handler)

    # register both functions
    server.register_function(string_reverse)
    server.register_function(string_length)

    server.register_function(queries.get_tr_by_prod_name)
    server.register_function(queries.get_tr_by_cus_id)
    server.register_function(queries.group_tr_by_store_id)
    server.register_function(queries.order_tr_by_payment)
    server.register_function(queries.get_city_by_store_id)

    server.register_function(database.insert_xml_document)
    server.register_function(database.soft_delete_xml_document)

    # start the server
    print("Starting the RPC Server...")
    server.serve_forever()
