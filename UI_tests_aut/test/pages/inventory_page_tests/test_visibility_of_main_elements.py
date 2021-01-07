from softest import TestCase

from test.base.test_case_base import TestCaseBase
import softest

from wait_factory.explicit_wait_factory import WaitFactory


class TestInventoryPageLayout(TestCaseBase):

    def setup_method(self):
        self.driver = TestCaseBase.get_driver()
        self.page = TestCaseBase.get_pages_model().get_inventory_page()
        self.page_header = self.page.get_header_section()
        self.page_inventory = self.page.get_inventory_section()
        self.page_footer = self.page.get_footer_section()

    # def test_visibility_of_header_elements(self):
    def test_the_elements(self):
    # print("_ - - _ - - _ - - _ -- ")
        self.page_header.menu_burger_button.click()

        self.header_elements = self.page_header.get_sidebars_elements()
        print(type(self.header_elements))

        self.header_elements[0].click()
    # # self.soft_assert(self.assertTrue(header_elements.))
    # self.assert_all()
