from csv_to_xml_converter import CSVtoXMLConverter

if __name__ == "__main__":
    converter = CSVtoXMLConverter("/data/Retail_Transactions_Dataset.csv")
    # converter.to_xml_file()
    # print(converter.to_xml_str())
    converter.validate_xml('/data/schema.xsd', '/data/retail.xml')
