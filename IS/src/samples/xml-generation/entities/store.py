import xml.etree.ElementTree as ET


class Store:

    def __init__(self, name, city):
        Store.counter += 1
        self._id = Store.counter
        self._name = name
        self._city_ref = city

    def to_xml(self):
        store_el = ET.Element("Store")
        store_el.set("ID", self.get_id())

        name_el = ET.Element("Type")
        name_el.text = self._name
        store_el.append(name_el)

        city_el = ET.Element("City")
        city_el.text = self._city_ref
        store_el.append(city_el)

        return store_el

    def get_id(self):
        return str("s") + str(self._id)

    def __str__(self):
        return f"name: {self._name}, id:{self._id}, city_ref:{self._city_ref}"


Store.counter = 0
