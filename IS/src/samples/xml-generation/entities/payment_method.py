import xml.etree.ElementTree as ET


class Payment_Method:

    def __init__(self, method):
        Payment_Method.counter += 1
        self._id = Payment_Method.counter
        self._method = method

    def to_xml(self):
        el = ET.Element("Payment_Method")
        el.set("id", self.get_id())
        el.set("Method", self._method)
        return el

    def get_id(self):
        return str("p") + str(self._id)

    def __str__(self):
        return f"name: {self._method}, id:{self._id}"


Payment_Method.counter = 0
