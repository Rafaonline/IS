import xml.etree.ElementTree as ET


class Transaction:

    def __init__(self, date, customer, product, total_items, value, payment_method, store):
        Transaction.counter += 1
        self._id = Transaction.counter
        self._date = date
        self._customer = customer
        self._product = product
        self._total_items = total_items
        self._value = value
        self._payment_method = payment_method
        self._store = store

    def to_xml(self):
        el = ET.Element("Transaction")
        el.set("id", str("tr") + str(self._id))
        el.set("Date", self._date)
        el.set("Customer", self._customer)
        el.set("Product", self._product)
        el.set("Total_Items", self._total_items)
        el.set("Value", self._value)
        el.set("Payment_Method", self._payment_method)
        el.set("Store", self._store)

        return el

    def get_id(self):
        return self._id

    def __str__(self):
        return f"date: {self._date}, id:{self._id}, customer:{self._customer}"


Transaction.counter = 0
