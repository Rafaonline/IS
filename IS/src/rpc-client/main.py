import xmlrpc.client
import xml.etree.ElementTree as ET

print("connecting to server...")
server = xmlrpc.client.ServerProxy('http://is-rpc-server:9000')



def print_options():
    print("Options:")
    print("1 - STR reverse/ search tr by product")
    print("2 - STR length")
    print("0 - Exit")


while True:
    print_options()
    choice = input("Enter your choice (0 to exit): ")
    string = "hello world"

    if choice == "1":
        product_name = input("Enter a product name: ")
        product_id_query = (f"SELECT xpath('//Products/Product[@name=\"{product_name}\"]/@id', xml) "
                            f"FROM public.imported_documents;")
        product_id_result = server.execute_query(product_id_query)
        product_id = product_id_result[0]

        transaction_query = (f"SELECT xpath('//Transaction[Products/Product/@id=\"{product_id}\"]/@ID', xml) "
                             f"FROM public.imported_documents;")
        transaction_id_result = server.execute_query(transaction_query)

        if transaction_id_result:

            for transaction_id_list in transaction_id_result:
                transaction_id = transaction_id_list[0]

                # Remover os caracteres especiais e quebras de linha do início e do final da string
                transaction_id = transaction_id.strip('{}').replace(',', '\n')

                print("\nTransactions ID:")
                print()
                print(transaction_id)
        else:
            print("There aren't any transactions id refering this product.")

        print(f" > {server.string_reverse(string)}")
    elif choice == "2":
        print(f" > {server.string_length(string)}")
    elif choice == "0":
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again.")

