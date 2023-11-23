import xml.etree.ElementTree as ET


class Store:

    def __init__(self, name, city):
        Store.counter += 1
        self._id = Store.counter
        self._name = name
        self._city_ref = city

    def to_xml(self):
        el = ET.Element("Store")
        el.set("id", str("s") + str(self._id))
        el.set("Store", self._name)
        el.set("City_Ref", str("c") + str(self._city_ref.get_id()))
        return el

    def __str__(self):
        return f"name: {self._name}, id:{self._id}, city_ref:{self._city_ref}"


Store.counter = 0
