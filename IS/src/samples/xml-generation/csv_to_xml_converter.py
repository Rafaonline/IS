import csv
import xml.dom.minidom as md
import xml.etree.ElementTree as ET

from csv_reader import CSVReader

from entities.city import City
from entities.store import Store
from entities.produto import Produto
from entities.customer import Customer
"""
from entities.produtos import Produtos
from entities.team import Team
from entities.player import Player
"""


class CSVtoXMLConverter:

    def __init__(self, path):
        self._reader = CSVReader(path)

    def to_xml(self):
        # read city

        cities = self._reader.read_entities(
            attr="City",
            builder=lambda row: City(row["City"])
        )

        # read stores
        stores = self._reader.read_entities(
            attr="Store_Type",
            builder=lambda row: Store(row["Store_Type"])
        )

        produtos = self._reader.read_entities(
            attr="Product",
            builder=lambda row: Produto(row["Product"])
        )

        customers = self._reader.read_entities(
            attr="Customer_Name",
            builder=lambda row: Customer(row["Customer_Name"])
        )


        """

        # read teams
        teams = self._reader.read_entities(
            attr="Current Club",
            builder=lambda row: Team(row["Current Club"])
        )

        # read players

        def after_creating_player(player, row):
            # add the player to the appropriate team
            teams[row["Current Club"]].add_player(player)

        self._reader.read_entities(
            attr="full_name",
            builder=lambda row: Player(
                name=row["full_name"],
                age=row["age"],
                country=countries[row["nationality"]]
            ),
            after_create=after_creating_player
        )

        # generate the final xml
        root_el = ET.Element("Football")

        teams_el = ET.Element("Teams")
        for team in teams.values():
            teams_el.append(team.to_xml())

        countries_el = ET.Element("Countries")
        for country in countries.values():
            countries_el.append(country.to_xml())

        root_el.append(teams_el)
        root_el.append(countries_el)
"""

        root_el = ET.Element("Retail")

        city_el = ET.Element("City")
        for city in cities.values():
            city_el.append(city.to_xml())

        store_el = ET.Element("Store_Type")
        for store in stores.values():
            store_el.append(store.to_xml())

        produto_el = ET.Element("Product")
        for produto in produtos.values():
            produto_el.append(produto.to_xml())

        customer_el = ET.Element("Customer_Name")
        for customer in customers.values():
            customer_el.append(customer.to_xml())

        root_el.append(produto_el)
        root_el.append(store_el)
        root_el.append(city_el)

        """root_el.append(customer_el)"""

        return root_el

    def to_xml_str(self):
        xml_str = ET.tostring(self.to_xml(), encoding='utf8', method='xml').decode()
        dom = md.parseString(xml_str)
        return dom.toprettyxml()

