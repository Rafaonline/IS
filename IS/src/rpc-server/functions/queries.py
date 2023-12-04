import psycopg2

from db.db_conn import DatabaseConnection


class Queries:
    def __int__(self):
        self.db = DatabaseConnection()

    def get_tr_by_prod_name(self, product_name):

        product_id_query = (f"SELECT xpath('//Products/Product[@name=\"{product_name}\"]/@id', xml) "
                            f"FROM public.imported_documents;")

        product_id_result = self.db.execute_query(product_id_query)
        product_id = product_id_result[0]

        transaction_query = (f"SELECT xpath('//Transaction[Products/Product/@id=\"{product_id}\"]', xml) "
                             f"FROM public.imported_documents;")
        result = self.db.execute_query(transaction_query)

        return result

    def get_tr_by_cus_id(self, id_client):
        query = (f"SELECT xpath('//Transaction[Customer[@ID=\"{id_client}\"]]', xml) "
                 f"FROM public.imported_documents ")
        result = self.db.execute_query(query)

        return result

    def order_tr_by_payment(self):
        query = (f"SELECT unnest(xpath('//Transaction/@ID', xml))::text as transaction_id, "
                 f"unnest(xpath('//Transaction/Payment/@Value', xml))::text as payment_value "
                 f"FROM imported_documents "
                 f"ORDER BY CAST(unnest(xpath('//Transaction/Payment/@Value', xml))::text AS DECIMAL);")
        result = self.db.execute_query(query)

        return result

    def group_tr_by_store_id(self):
        query = (f"SELECT unnest(xpath('//Transaction/Store/@ID', xml))::text as store_id, "
                 f"COUNT(*) as number_of_transactions FROM imported_documents "
                 f"GROUP BY store_id "
                 f"ORDER BY number_of_transactions; ")
        result = self.db.execute_query(query)

        return result

    def get_city_by_store_id(self, store_id):
        query = (f"SELECT unnest(xpath('//Store_Types/Store[@ID=\"{store_id}\"]/@ID', xml))::text AS StoreID, "
                 f"unnest(xpath('//Store_Types/Store[@ID=\"{store_id}\"]/Type/text()', xml))::text AS StoreType, "
                 f"unnest(xpath('//Cities/City[@id=//Store_Types/Store[@ID=\"{store_id}\"]/City/@id]/@name', xml)) AS CityName, "
                 f"unnest(xpath('//Cities/City[@id=//Store_Types/Store[@ID=\"{store_id}\"]/City/@id]/Latitude/text()', xml))::text AS Latitude, "
                 f"unnest(xpath('//Cities/City[@id=//Store_Types/Store[@ID=\"{store_id}\"]/City/@id]/Longitude/text()', xml))::text AS Longitude "
                 f"FROM public.imported_documents; ")
        result = self.db.execute_query(query)

        return result
