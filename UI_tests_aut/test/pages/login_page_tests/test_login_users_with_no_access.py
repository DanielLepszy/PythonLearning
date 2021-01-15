import pytest
from UI_tests_aut.main.read_data.properties.read_properties import PropertiesReader
from UI_tests_aut.test.base.test_case_base import TestCaseBase
from read_data.json_data.login_page.json_reader import UserCredentialsReaderInterface


# @pytest.mark.skipif(PropertiesReader.if_save_running_time(), reason="Ignore test to save time running")
@pytest.mark.functional
class TestLoginToAppByAllUsersType(TestCaseBase):
    users_with_no_access = UserCredentialsReaderInterface.get_user_with_no_access()

    def setup_method(self):
        self.driver = TestCaseBase.get_driver()
        self.page = TestCaseBase.get_pages_model().get_login_page()
        self.url = PropertiesReader().load_properties_from_file('url').data

    @pytest.mark.parametrize("arg", users_with_no_access)
    def test_validation(self, arg):
        self.driver.get(self.url)
        username = arg.get('username')
        password = arg.get('password')
        error_message = arg['validation_error_messages'].get('message')

        self.page.set_credentials_to_inputs(username, password)
        if self.driver.current_url !='https://www.saucedemo.com/':
            raise Exception

        self.error_validation_message = self.page.error_header.text
        print(f'Assert error message for username: {username} and password: {password}')
        assert self.error_validation_message == error_message

