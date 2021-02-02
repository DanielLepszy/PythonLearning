import pytest

from page_models.page_models_factory.pages.inventory_page.sections.header_section import FilterValueEnum
from read_data.properties.read_properties import PropertiesReader
from test.base.test_case_base import TestCaseBase

@pytest.mark.skipif(PropertiesReader.if_save_running_time(), reason="Ignore test to save time running")
@pytest.mark.order(3)
@pytest.mark.filtering
class TestAddToCardAFewItems(TestCaseBase):

    def setup_method(self):
        self.driver = TestCaseBase.get_driver()
        self.driver.get('https://www.saucedemo.com/inventory.html')
        self.page = TestCaseBase.get_pages_model().get_inventory_page()
        self.page_header = self.page.get_header_section()
        self.page_inventory = self.page.get_inventory_section()
        items = self.page_inventory.get_card_item_elements()
        self.prices = [float(x.price.text[1:]) for x in items]
        self.names = [x.name.text for x in items]

    def test_filtering_items_price_asc(self):
        sorted_prices = self.page_header.filtering_ascending_items_price(self.prices)
        self.page_header.select_filter(FilterValueEnum.PRICE_ASC.value)

        sorted_items = self.page_inventory.get_card_item_elements()
        sorted_prices_in_page = tuple([float(x.price.text[1:]) for x in sorted_items])

        assert sorted_prices == sorted_prices_in_page

    def test_filtering_items_name_desc(self):
        sorted_names = self.page_header.filtering_descending_items_name(self.names)
        self.page_header.select_filter(FilterValueEnum.PRICE_ASC.value)

        sorted_items = self.page_inventory.get_card_item_elements()
        sorted_names_in_page = tuple([float(x.price.text[1:]) for x in sorted_items])

        assert sorted_names == sorted_names_in_page

