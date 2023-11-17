import xml.etree.ElementTree as ET


class Customer:

    def __init__(self, name):
        Customer.counter += 1
        self._id = Customer.counter
        self._name = name

    def to_xml(self):
        el = ET.Element("Customer_Name")
        el.set("id", str("cus") + str(self._id))
        el.set("Customer_Name", self._name)
        return el

    def get_id(self):
        return self._id

    def __str__(self):
        return f"name: {self._name}, id:{self._id}"


Customer.counter = 0