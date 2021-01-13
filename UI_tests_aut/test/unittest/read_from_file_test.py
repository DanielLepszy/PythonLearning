from unittest.mock import Mock

# from properties.read_properties import PropertiesReader
from UI_tests_aut.main.properties.read_properties import PropertiesReader


def test_get_property_from_file():

    bar = Mock(spec=PropertiesReader)
    # bar2 = Mock(side_effect=barFunc)
    # bar3 = Mock(return_value=1)

    # def load_properties_from_file(cls, key_property):
#     configs = Properties()
#     # with open('../test_config.properties', 'rb') as config_file:
#     with open(
#             "C:/Users/Daniel_Lepszy/Tools/PythonLearningProject/PythonLearnCode/UI_tests_aut/test_config.properties",
#             'rb') as config_file:
#         configs.load(config_file)
#
#         return configs.get(key_property)
