import csv
import xml.dom.minidom as md
import xml.etree.ElementTree as ET
import ast

from csv_reader import CSVReader

from entities.city import City
from entities.store import Store
from entities.produto import Produto
from entities.category import Category
from entities.customer import Customer
from entities.payment_method import Payment_Method
from entities.transaction import Transaction
"""
from entities.produtos import Produtos
from entities.team import Team
from entities.player import Player
"""


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
            builder=lambda row, key: Produto(key),
            get_keys=lambda row:  ast.literal_eval(row["Product"])
        )

        # read customers
        customers = self._reader.read_entities(
            get_keys=lambda row: f'{row["Customer_Name"]}_{row["Customer_Category"]}',
            builder=lambda row, _: Customer(name=row["Customer_Name"], category=["Customer_Category"])
        )

        # read categories
        category = self._reader.read_entities(
            get_keys=lambda row: row["Customer_Category"],
            builder=lambda row, _: Category(row["Customer_Category"])
        )

        # read payment method
        payment_method = self._reader.read_entities(
            get_keys=lambda row: row["Payment_Method"],
            builder=lambda row, _: Payment_Method(row["Payment_Method"])
        )

        # read transaction
        transaction = self._reader.read_entities(
            get_keys=lambda row: f'{row["Date"]}_{row["Customer_Name"]}',
            builder=lambda row, _: Transaction(date=row["Date"], customer=["Customer_Name"], product=row["Product"],
                                               total_items=row["Total_Items"], value=row["Total_Cost"],
                                               payment_method=row["Payment_Method"], store=row["Store_Type"])
        )

        root_el = ET.Element("Retail")

        city_el = ET.Element("City")
        for city in cities.values():
            city_el.append(city.to_xml())

        store_el = ET.Element("Store_Type")
        for store in stores.values():
            store_el.append(store.to_xml())

        products_el = ET.Element("Product")
        for products in products.values():
            products_el.append(products.to_xml())

        category_el = ET.Element("Customer_Category")
        for category in category.values():
            category_el.append(category.to_xml())

        customer_el = ET.Element("Customer_Name")
        for customer in customers.values():
            customer_el.append(customer.to_xml())

        payment_method_el = ET.Element("Payment_Method")
        for payment_method in payment_method.values():
            payment_method_el.append(payment_method.to_xml())

        transaction_el = ET.Element("Transaction")
        for transaction in transaction.values():
            transaction_el.append(transaction.to_xml())

        root_el.append(products_el)
        root_el.append(store_el)
        root_el.append(city_el)
        root_el.append(category_el)
        root_el.append(customer_el)
        root_el.append(payment_method_el)
        root_el.append(transaction_el)

        return root_el

    def to_xml_str(self):
        xml_str = ET.tostring(self.to_xml(), encoding='utf8', method='xml').decode()
        dom = md.parseString(xml_str)
        return dom.toprettyxml()
