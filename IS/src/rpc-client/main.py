import xmlrpc.client

print("connecting to server...")
server = xmlrpc.client.ServerProxy('http://is-rpc-server:9000')


# list all transactions by product name
def tr_by_prod_name(product_name):
    try:
        transactions = server.get_tr_id_by_prod_name(product_name)

        if transactions:
            print(f"Every transaction with {product_name} included.")
            for tr in transactions:
                print(f"\n -> {tr}")
        else:
            print(f"There aren't any transactions with {product_name} included.")
    except Exception as e:
        print(f"Error: {e}")


def print_options():
    print("Options:")
    print("1 - STR reverse/ search tr by product")
    print("2 - STR length")
    print("0 - Exit")


def main():
    while True:
        print_options()
        choice = input("Enter your choice (0 to exit): ")
        string = "hello world"

        if choice == "1":
            tr_by_prod_name("Hair Gel")
        elif choice == "2":
            print(f" > {server.string_length(string)}")
        elif choice == "0":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
