import pytest
from delayed_assert import expect, delayed_assert
from selenium.webdriver.common.by import By
from UI_tests_aut.main.wait_factory.explicit_wait_factory import WaitFactory
from UI_tests_aut.test.base.test_case_base import TestCaseBase
from UI_tests_aut.main.read_data.properties.read_properties import PropertiesReader


@pytest.mark.skipif(PropertiesReader.if_save_running_time(), reason="Ignore test to save time running")
@pytest.mark.layout
class TestInventoryPageLayout(TestCaseBase):

    def setup_class(self):
        self.driver = self.get_driver()
        self.driver.get("https://www.saucedemo.com/inventory.html")
        self.page = self.get_pages_model().get_inventory_page()

    @pytest.fixture()
    def close_sidebar(self):
        yield
        self.page_header.cross_sidebar_button.click()
        WaitFactory.wait_until_element_invisible(self.driver, By.CSS_SELECTOR, 'bm-menu')

    @delayed_assert.assert_all()
    def test_footer_section(self):
        self.page_footer = self.page.get_footer_section()
        for el in self.page_footer.get_footer_elements(): expect(el.is_displayed())

    @delayed_assert.assert_all()
    def test_header_section(self, close_sidebar):
        self.page_header = self.page.get_header_section()
        '''Headers logo'''
        expect(self.page_header.shopping_trolley_icon.is_displayed())
        expect(self.page_header.app_logo.is_displayed())
        expect(self.page_header.product_label.text == 'Products')

        '''Sidebars elements'''
        self.page_header.menu_burger_button.click()
        self.header_elements = self.page_header.get_sidebars_elements()
        expect(len(self.header_elements) == 4)
        for el in self.header_elements: expect(el.is_displayed())

    @delayed_assert.assert_all()
    def test_inventory_section(self):
        self.page_inventory = self.page.get_inventory_section()

        card_models = self.page_inventory.get_card_item_elements()
        if len(card_models) == 6:
            for card in card_models:
                expect(card.image.is_displayed())
                expect(card.price.is_displayed())
                expect(card.add_card.is_displayed())
        else:
            raise Exception
