import xml.etree.ElementTree as ET


class Store:

    def __init__(self, type, city):
        Store.counter += 1
        self._id = Store.counter
        self._type = type
        self._city_ref = city

    def to_xml(self):
        store_el = ET.Element("Store")
        store_el.set("ID", self.get_id())

        type_el = ET.Element("Type")
        type_el.text = self._type
        store_el.append(type_el)

        city_el = ET.Element("City")
        city_el.set("id", self._city_ref.get_id())
        store_el.append(city_el)

        return store_el

    def get_id(self):
        return str("s") + str(self._id)

    def __str__(self):
        return f"name: {self._type}, id:{self._id}, city_ref:{self._city_ref}"


Store.counter = 0
