import pytest
from UI_tests_aut.main.properties.read_properties import Properties_Reader
from browsers_model.browsers import Browsers


@pytest.mark.order(1)
class TestClass:

    def setup_class(self):
        Browsers(Properties_Reader().load_properties_from_file('browser_type').data)
        self.driver = Browsers.get_driver()
        self.url = Properties_Reader().load_properties_from_file('url').data

    def test_open(self):
        self.driver.get(self.url)
        assert self.driver.current_url == self.url

    #
    # def teardown_class(self):
    #     self.driver.close()
