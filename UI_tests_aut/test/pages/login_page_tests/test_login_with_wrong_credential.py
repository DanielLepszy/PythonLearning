import pytest

from test.base.test_case_base import TestCaseBase


@pytest.mark.order(3)
class TestLoginWithWrongCredential(TestCaseBase):

    def setup_method(self):
        self.driver = TestCaseBase.get_driver()
        self.page = TestCaseBase.get_pages_model().get_login_page()

    def test_validation_input(self):
        self.page.set_credentials_to_inputs('username', 'password')
        self.error_validation_message = self.page.error_header.text

        assert self.error_validation_message == 'Epic sadface: Username and password do not match any user in this service'
