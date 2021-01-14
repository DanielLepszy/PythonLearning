import pytest

from UI_tests_aut.main.read_data.read_properties import PropertiesReader
from UI_tests_aut.test.base.test_case_base import TestCaseBase

@pytest.mark.skipif(PropertiesReader.if_save_running_time(), reason="Ignore test to save time running")
@pytest.mark.order(6)
@pytest.mark.functional
class TestLogout(TestCaseBase):

    def setup_method(self):
        self.driver = TestCaseBase.get_driver()
        self.page = TestCaseBase.get_pages_model().get_inventory_page()
        self.page_header = self.page.get_header_section()

    def test_logout_action(self):
        if self.page.get_page_url() != self.driver.current_url:
            raise Exception
        else:
            self.page_header.logout_from_app()

        assert self.driver.current_url == 'https://www.saucedemo.com/index.html'
