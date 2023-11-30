import json
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET


class City:

    def __init__(self, name):
        City.counter += 1
        self._id = City.counter
        self._name = name
        self._latitude = None
        self._longitude = None
        self.fetch_coordinates()

    def fetch_coordinates(self):
        # Use Nominatim API to fetch coordinates for the country
        endpoint = "https://nominatim.openstreetmap.org/search"
        params = {
            "q": self._name,
            "format": "json",
            "limit": 1,
        }
        url = f"{endpoint}?{urllib.parse.urlencode(params)}"

        with urllib.request.urlopen(url) as response:
            data = json.load(response)
            if data:
                location = data[0]
                self._latitude = location.get("lat")
                self._longitude = location.get("lon")

    def to_xml(self):
        city_el = ET.Element("City")
        city_el.set("id", self.get_id())
        city_el.set("name", self._name)

        lat_el = ET.Element("Latitude")
        lat_el.text = self._latitude
        city_el.append(lat_el)

        lon_el = ET.Element("Longitude")
        lon_el.text = self._longitude
        city_el.append(lon_el)

        return city_el

    def get_id(self):
        return str("c") + str(self._id)

    def __str__(self):
        return f"name: {self._name}, id:{self._id}"


City.counter = 0
