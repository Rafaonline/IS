from csv import DictReader


class CSVReader:

    def __init__(self, path, delimiter=','):
        self._path = path
        self._delimiter = delimiter

    def loop(self):
        with open(self._path, 'r') as file:
            for row in DictReader(file, delimiter=self._delimiter):
                yield row
        file.close()

    @staticmethod
    def __process_entity(entities, row, key, builder, after_create=None):
        if key not in entities:
            entities[key] = builder(row, key)
            if after_create is not None:
                after_create(entities[key], row)

    def read_entities(self, builder, after_create=None, get_keys=None):
        entities = {}
        for row in self.loop():
            keys = get_keys(row)
            if isinstance(keys, str):
                keys = [keys]

            for key in keys:
                CSVReader.__process_entity(entities, row, key, builder, after_create)

        return entities
