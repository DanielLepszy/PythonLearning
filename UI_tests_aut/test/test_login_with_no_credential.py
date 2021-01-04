import pytest

from test.test_case_base import Test_Case_Base


@pytest.mark.order(3)
class Test_Login_With_No_Credential(Test_Case_Base):


    def setup_class(self):
        self.driver = Test_Case_Base.get_driver()

    @pytest.fixture()
    def prepare_elements(self):
        self.username_input = self.driver.find_element_by_id('user-name')
        self.password_input = self.driver.find_element_by_id('password')
        self.login_button = self.driver.find_element_by_id('login-button')
        self.error_header_css = 'h3[data-test="error"]'

    def test_validation_input(self, prepare_elements):
        self.username_input.send_keys('username_test')
        self.password_input.send_keys('password_test')
        self.login_button.click()
        self.error_validation_message = self.driver.find_element_by_css_selector(self.error_header_css).text

        assert self.error_validation_message == 'Epic sadface: Username and password do not match any user in this service'

