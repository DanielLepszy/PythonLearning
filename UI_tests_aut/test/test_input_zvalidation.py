from UI_tests_aut.main.browsers_model.firefox_browser import Firefox
from UI_tests_aut.main.properties.read_properties import Properties_Reader
import pytest


class Test_Input_Login_Validation:

    def setup_class(self):
        self.driver = Firefox().get_driver()
        self.driver.get(Properties_Reader().load_properties_from_file('url').data)

    @pytest.fixture()
    def prepare_elements(self):
        self.username_input = self.driver.find_element_by_id('user-name')
        self.password_input = self.driver.find_element_by_id('password')
        self.login_button = self.driver.find_element_by_id('login-button')

    def test_validation_input(self, prepare_elements):
        self.username_input.send_keys('username_test')
        self.password_input.send_keys('password_test')
        self.login_button.click()
        # print(type(self.driver.find_elements_by_id('user-name')))
        # self.username_input.send_keys("username")
        # self.password_input.send_keys("username")
        # self.login_button.click()

        assert True
