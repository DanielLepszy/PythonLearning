from jproperties import Properties

class PropertiesReader():

    def load_properties_from_file(self, property):
        configs = Properties()
        # with open('../test_config.properties', 'rb') as config_file:
        with open("C:/Users/Daniel_Lepszy/Tools/PythonLearningProject/PythonLearnCode/UI_tests_aut/test_config.properties", 'rb') as config_file:
            configs.load(config_file)

            return configs.get(property)