from csv_to_xml_converter import CSVtoXMLConverter

if __name__ == "__main__":
    converter = CSVtoXMLConverter("/data/Retail_Transactions_Dataset.csv")
    converter.to_xml_file()
