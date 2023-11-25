import xml.dom.minidom as md
import xml.etree.ElementTree as ET
import ast

from csv_reader import CSVReader

from entities.city import City
from entities.store import Store
from entities.produto import Product
from entities.customer import Customer
from entities.transaction import Transaction


class CSVtoXMLConverter:

    def __init__(self, path):
        self._reader = CSVReader(path)

    def to_xml(self):
        # read city

        cities = self._reader.read_entities(
            builder=lambda row, _: City(row["City"]),
            get_keys=lambda row: row["City"]
        )

        # read stores
        stores = self._reader.read_entities(
            get_keys=lambda row: f'{row["Store_Type"]}_{row["City"]}',
            builder=lambda row, _: Store(name=row["Store_Type"], city=cities[row["City"]])
        )

        # read products
        products = self._reader.read_entities(
            builder=lambda row, key: Product(key),
            get_keys=lambda row:  ast.literal_eval(row["Product"])
        )

        # read customers
        customers = self._reader.read_entities(
            get_keys=lambda row: f'{row["Customer_Name"]}_{row["Customer_Category"]}',
            builder=lambda row, _: Customer(name=row["Customer_Name"], category=row["Customer_Category"])
        )

        # read transaction
        transaction = self._reader.read_entities(
            get_keys=lambda row: row["Transaction_ID"],
            builder=lambda row, _: Transaction(date=row["Date"],
                                               customer=customers[f'{row["Customer_Name"]}_{row["Customer_Category"]}'],
                                               products=[products[key] for key in ast.literal_eval(row["Product"])],
                                               total_items=row["Total_Items"],
                                               value=row["Total_Cost"],
                                               payment_method=row["Payment_Method"],
                                               store=stores[f'{row["Store_Type"]}_{row["City"]}'],
                                               discount=row["Discount_Applied"],
                                               season=row["Season"],
                                               promotion=row["Promotion"]
                                               )
        )

        root_el = ET.Element("Retail")

        city_el = ET.Element("Cities")
        for city in cities.values():
            city_el.append(city.to_xml())

        store_el = ET.Element("Store_Types")
        for store in stores.values():
            store_el.append(store.to_xml())

        products_el = ET.Element("Products")
        for products in products.values():
            products_el.append(products.to_xml())

        customer_el = ET.Element("Customers")
        for customer in customers.values():
            customer_el.append(customer.to_xml())

        transaction_el = ET.Element("Transactions")
        for transaction in transaction.values():
            transaction_el.append(transaction.to_xml())

        #root_el.append(products_el)
        #root_el.append(store_el)
        #root_el.append(city_el)
        #root_el.append(customer_el)
        #root_el.append(transaction_el)

        return root_el

    def to_xml_str(self):
        xml_str = ET.tostring(self.to_xml(), encoding='utf8', method='xml').decode()
        dom = md.parseString(xml_str)
        return dom.toprettyxml()

    def to_xml_file(self, filename='retail.xml'):
        root_el = self.to_xml()
        xml_str = ET.tostring(root_el, encoding='utf-8').decode('utf-8')
        dom = md.parseString(xml_str)

        with open(filename, 'w', encoding='utf-8') as xml_file:
            xml_file.write(dom.toprettyxml(indent='\t'))

