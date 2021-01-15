import pytest
from UI_tests_aut.main.read_data.properties.read_properties import PropertiesReader
from UI_tests_aut.test.base.test_case_base import TestCaseBase
from UI_tests_aut.main.read_data.json_data.login_page.user_log_in_interface import UserLogInReaderInterface, UserType


@pytest.mark.skipif(PropertiesReader.if_save_running_time(), reason="Ignore test to save time running")
@pytest.mark.order(2)
@pytest.mark.functional
class TestLoginToAccount(TestCaseBase):

    def setup_method(self):
        self.driver = TestCaseBase.get_driver()
        self.page = TestCaseBase.get_pages_model().get_login_page()
        self.username = UserLogInReaderInterface.get_username(UserType.STANDARD)
        self.password = UserLogInReaderInterface.get_password(UserType.STANDARD)

    def test_validation(self):
        self.page.set_credentials_to_inputs(self.username, self.password)
        assert self.driver.current_url == 'https://www.saucedemo.com/inventory.html'
