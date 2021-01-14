import pytest
from UI_tests_aut.main.read_data.read_properties import PropertiesReader
from UI_tests_aut.test.base.test_case_base import TestCaseBase

@pytest.mark.skipif(PropertiesReader.if_save_running_time(), reason="Ignore test to save time running")
@pytest.mark.order(4)
@pytest.mark.functional
class TestLoginToAccount(TestCaseBase):

    def setup_method(self):
        self.driver = TestCaseBase.get_driver()
        self.page = TestCaseBase.get_pages_model().get_login_page()
        self.username = PropertiesReader.get_value('username').data
        self.password = PropertiesReader.get_value('password').data

    def test_validation(self):
        self.page.set_credentials_to_inputs(self.username, self.password)
        assert self.driver.current_url == 'https://www.saucedemo.com/inventory.html'


