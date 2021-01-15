import pytest
from UI_tests_aut.main.read_data.properties.read_properties import PropertiesReader
from UI_tests_aut.test.base.test_case_base import TestCaseBase
from UI_tests_aut.main.read_data.json_data.login_page.user_log_in_interface import UserLogInReaderInterface


@pytest.mark.skipif(PropertiesReader.if_save_running_time(), reason="Ignore test to save time running")
@pytest.mark.data_driven_approach
class TestLoginToAppByAllUsersType(TestCaseBase):
    users_types_credentials = UserLogInReaderInterface.get_only_proper_users_credentials()

    def setup_method(self):
        self.driver = TestCaseBase.get_driver()
        self.page = TestCaseBase.get_pages_model().get_login_page()
        self.url = PropertiesReader().load_properties_from_file('url').data

    @pytest.mark.parametrize("username,password", users_types_credentials)
    def test_validation(self, username, password):
        self.driver.get(self.url)
        self.page.set_credentials_to_inputs(username, password)
        assert self.driver.current_url == 'https://www.saucedemo.com/inventory.html'
