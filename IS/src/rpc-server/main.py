import signal, sys
from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler
import xml.etree.ElementTree as ET
from functions.string_length import string_length
from functions.string_reverse import string_reverse


class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)
"""
def consultar_lojas():
    idloja = '/data/retail.xml'
    lojas = lojasxml(idloja)

    return lojas

def lojasxml(idloja):
    tree = ET.parse(idloja)
    root = tree.getroot()

    lojas = []

    for transaction_elem in root.findall('.//Transaction'):
        transaction_id = transaction_elem.get('ID')
        store_elem = transaction_elem.find('./Store')
        store_id = store_elem.get('ID') if store_elem is not None else None

        if store_id is not None:
            lojas.append({'transaction_id': transaction_id, 'store_id': store_id})

    return lojas
"""
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

    # start the server
    print("Starting the RPC Server...")
    server.serve_forever()
