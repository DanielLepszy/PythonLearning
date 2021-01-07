from test.base.test_case_base import TestCaseBase
from wait_factory.explicit_wait_factory import WaitFactory


class TestVisibilityOfInventoryElements(TestCaseBase):

    def setup_method(self):
        self.driver = TestCaseBase.get_driver()
        self.page = TestCaseBase.get_pages_model().get_inventory_page()

    def test_visibility_of_elements(self):
        WaitFactory.wait_until_visibility_of_element(self.driver, self.page.product)

        assert self.driver.current_url == self.page.get_page_url()