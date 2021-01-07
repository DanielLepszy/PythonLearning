import pytest
from properties.read_properties import PropertiesReader
from test.base.test_case_base import TestCaseBase


@pytest.mark.order(4)
class TestLoginToAccount(TestCaseBase):

    def setup_method(self):
        self.driver = TestCaseBase.get_driver()
        self.page = TestCaseBase.get_pages_model().get_login_page()
        self.username = PropertiesReader.get_value('username').data
        self.password = PropertiesReader.get_value('password').data

    def test_validation(self):
        self.page.set_credentials_to_inputs(self.username, self.password)
        assert self.driver.current_url == 'https://www.saucedemo.com/inventory.html'


