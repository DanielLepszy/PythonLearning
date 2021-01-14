import pytest
from jproperties import Properties

from UI_tests_aut.main.read_data.read_properties import PropertiesReader

@pytest.mark.unittest
class TestPropertyReaderInterface:

    def test_get_single_property_from_file(self):
        ## Given
        property = 'url'
        reader = PropertiesReader()

        ## When
        value = reader.load_properties_from_file(property).data
        ## Then
        assert value == 'https://www.saucedemo.com/'

    def test_FileNotFoundError(self):
        configs = Properties(self)
        with pytest.raises(FileNotFoundError):
            with open(
                    "Wrong_File_Path",
                    'rb') as config_file:
                configs.load(config_file)

    def test_wrong_property(self):
        prop = 'wrong_property_in_file'
        reader = PropertiesReader()

        value = reader.load_properties_from_file(prop)

        assert value is None

    def test_browser_values(self):
        prop = 'browser_type'
        accept_browser_type = {'firefox', 'chrome', 'edge', 'explorer', 'safari', 'opera'}
        reader = PropertiesReader()

        value = reader.load_properties_from_file(prop).data

        assert value in accept_browser_type

    def test_save_time_values(self):
        reader = PropertiesReader()
        value = reader.if_save_running_time()

        assert value is True | False

    def test_username_values(self):
        prop = 'username'
        accept_username_type = {'standard_user', 'locked_out_user', 'problem_user', 'performance_glitch_user'}
        reader = PropertiesReader()

        value = reader.load_properties_from_file(prop).data

        assert value in accept_username_type

    def test_password_values(self):
        prop = 'password'
        reader = PropertiesReader()
        value = reader.load_properties_from_file(prop).data
        assert value == 'secret_sauce'
