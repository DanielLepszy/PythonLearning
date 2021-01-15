import pytest
from UI_tests_aut.main.read_data.properties.read_properties import PropertiesReader
from UI_tests_aut.test.base.test_case_base import TestCaseBase
from read_data.json_data.login_page.json_reader import UserCredentialsReaderInterface


# @pytest.mark.skipif(PropertiesReader.if_save_running_time(), reason="Ignore test to save time running")
@pytest.mark.functional
class TestLoginToAppByAllUsersType(TestCaseBase):

    def setup_method(self):
        self.driver = TestCaseBase.get_driver()
        self.page = TestCaseBase.get_pages_model().get_login_page()
        self.url = PropertiesReader().load_properties_from_file('url').data

    @pytest.fixture()
    def all_users_types_credentials(self):
        users_credentials = UserCredentialsReaderInterface.get_only_proper_users_credentials()
        for user_credential in users_credentials:
            yield user_credential

    @pytest.mark.parametrize('user_credential', all_users_types_credentials())
    def test_validation(self, user_credential: tuple):
        self.driver.get(self.url)
        # TODO How to set test twice
        self.page.set_credentials_to_inputs(user_credential.index(0), user_credential.index(1))
        assert self.driver.current_url == 'https://www.saucedemo.com/inventory.html'

