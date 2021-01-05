import pytest
from UI_tests_aut.main.properties.read_properties import PropertiesReader
from test.base.test_case_base import TestCaseBase


@pytest.mark.order(1)
class TestClass(TestCaseBase):

    def setup_class(self):
        self.driver = TestCaseBase.set_driver()
        self.url = PropertiesReader().load_properties_from_file('url').data

    def test_open(self):
        ''' implicit wait for all web-elements'''
        self.driver.implicitly_wait(2)
        self.driver.get(self.url)
        assert self.driver.current_url == 'https://www.saucedemo.com/'
