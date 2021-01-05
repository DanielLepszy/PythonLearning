from jproperties import Properties

class PropertiesReader():

    def load_properties_from_file(self, property):
        configs = Properties()
        with open('../test_config.properties', 'rb') as config_file:
            configs.load(config_file)

            return configs.get(property)