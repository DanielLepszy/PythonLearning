import pytest

from test.base.test_case_base import TestCaseBase


@pytest.mark.order(2)
class Test_Empty_Inputs_Validations(TestCaseBase):

    def setup_class(self):
        self.driver = TestCaseBase.get_driver()

    @pytest.fixture()
    def prepare_elements(self):
        self.login_button = self.driver.find_element_by_id('login-button')
        self.error_header_css = 'h3[data-test="error"]'

    def test_validation(self, prepare_elements):
        self.login_button.click()
        self.error_validation_message = self.driver.find_element_by_css_selector(self.error_header_css).text

        assert self.error_validation_message == 'Epic sadface: Username is required'

