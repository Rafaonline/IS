import xml.etree.ElementTree as ET


class Store:

    def __init__(self, name):
        Store.counter += 1
        self._id = Store.counter
        self._name = name

    def to_xml(self):
        el = ET.Element("Store")
        el.set("id", str("s") + str(self._id))
        el.set("Store", self._name)
        return el

    def get_id(self):
        return self._id

    def __str__(self):
        return f"name: {self._name}, id:{self._id}"


Store.counter = 0