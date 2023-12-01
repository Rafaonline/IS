import xml.etree.ElementTree as ET


class Customer:

    def __init__(self, name, category):
        Customer.counter += 1
        self._id = Customer.counter
        self._name = name
        self._category = category

    def to_xml(self):
        customer_el = ET.Element("Customer")
        customer_el.set("ID", self.get_id())

        name_el = ET.Element("Name")
        name_el.text = self._name
        customer_el.append(name_el)

        category_el = ET.Element("Category")
        category_el.text = self._category
        customer_el.append(category_el)

        return customer_el

    def get_id(self):
        return str("cus") + str(self._id)

    def __str__(self):
        return f"name: {self._name}, id:{self._id}, category:{self._category}"


Customer.counter = 0
