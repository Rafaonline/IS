import xml.etree.ElementTree as ET


class Transaction:

    def __init__(self, name, category):
        Transaction.counter += 1
        self._id = Transaction.counter
        self._name = name
        self._category = category

    def to_xml(self):
        el = ET.Element("Customer_Name")
        el.set("id", str("cus") + str(self._id))
        el.set("Customer_Name", self._name)
        el.set("Customer_Category", self._category)
        return el

    def get_id(self):
        return self._id

    def __str__(self):
        return f"name: {self._name}, id:{self._id}, category:{self._category}"


Transaction.counter = 0
