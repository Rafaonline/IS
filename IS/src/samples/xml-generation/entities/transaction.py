import xml.etree.ElementTree as ET


class Transaction:

    def __init__(self, date, customer, products, total_items, value, payment_method, store, discount, season, promotion):
        Transaction.counter += 1
        self._id = Transaction.counter
        self._date = date
        self._customer = customer
        self._products = products
        self._total_items = total_items
        self._value = value
        self._payment_method = payment_method
        self._store = store
        self._discount = discount
        self._season = season
        self._promotion = promotion

    def to_xml(self):
        transaction_el = ET.Element("Transaction")
        transaction_el.set("ID", self.get_id())
        transaction_el.set("Date", self._date)

        store_el = ET.Element("Store")
        store_el.set("ID", self._store.get_id())
        transaction_el.append(store_el)

        costumer_el = ET.Element("Customer")
        costumer_el.set("ID", self._customer.get_id())
        transaction_el.append(costumer_el)

        products_el = ET.Element("Products")
        products_el.set("Total_Items", self._total_items)
        for product in self._products:
            product_el = ET.Element("Product", id=product.get_id())
            products_el.append(product_el)

        transaction_el.append(products_el)

        payment_el = ET.Element("Payment")
        payment_el.set("Method", self._payment_method)
        payment_el.set("Value", self._value)
        transaction_el.append(payment_el)

        details_el = ET.Element("Details")

        discount_el = ET.Element("Discount")
        discount_el.text = self._discount
        details_el.append(discount_el)

        season_el = ET.Element("Season")
        season_el.text = self._season
        details_el.append(season_el)

        promotion_el = ET.Element("Promotion")
        promotion_el.text = self._promotion
        details_el.append(promotion_el)

        transaction_el.append(details_el)

        return transaction_el

    def get_id(self):
        return str("tr") + str(self._id)

    def __str__(self):
        return f"date: {self._date}, id:{self._id}, customer:{self._customer}"


Transaction.counter = 0
