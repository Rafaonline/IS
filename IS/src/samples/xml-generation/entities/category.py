import xml.etree.ElementTree as ET


class Category:

    def __init__(self, category):
        Category.counter += 1
        self._id = Category.counter
        self._category = category

    def to_xml(self):
        el = ET.Element("Customer_Category")
        el.set("id", str("cus") + str(self._id))
        el.set("Category", self._category)
        return el

    def get_id(self):
        return self._id

    def __str__(self):
        return f"name: id:{self._id}, category:{self._category}"


Category.counter = 0
