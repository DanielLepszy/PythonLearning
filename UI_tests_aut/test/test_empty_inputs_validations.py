import pytest

from test.test_case_base import Test_Case_Base


@pytest.mark.order(2)
class Test_Empty_Inputs_Validations(Test_Case_Base):

    def setup_class(self):
        self.driver = Test_Case_Base.get_driver()

    @pytest.fixture()
    def prepare_elements(self):
        self.login_button = self.driver.find_element_by_id('login-button')
        self.error_header_css = 'h3[data-test="error"]'

    def test_validation(self, prepare_elements):
        self.login_button.click()
        self.error_validation_message = self.driver.find_element_by_css_selector(self.error_header_css).text

        assert self.error_validation_message == 'Epic sadface: Username is required'

