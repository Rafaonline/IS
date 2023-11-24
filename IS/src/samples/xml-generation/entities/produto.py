import xml.etree.ElementTree as ET


class Product:
    counter = 0

    def __init__(self, name):
        Product.counter += 1
        self._id = Product.counter
        self._name = name

    def to_xml(self):
        el = ET.Element("Product")
        el.set("id", self.get_id())
        el.set("name", self._name)
        return el

    def get_id(self):
        return str("p") + str(self._id)

    def __str__(self):
        return f"name: {self._name}, id:{self._id}"

