import xml.etree.ElementTree as ET

class Produto:
    counter = 0

    def __init__(self, name):
        Produto.counter += 1
        self.id = Produto.counter
        self._name = name

    def to_xml(self):
        el = ET.Element("Produto")
        el.set("id", "p" + str(self.id))
        el.set("name", self._name)
        return el

    def get_id(self):
        return self.id

    def __str__(self):
        return f"name: {self._name}, id:{self.id}"

