import pytest

from properties.read_properties import PropertiesReader
from test.base.test_case_base import TestCaseBase


@pytest.mark.skipif(PropertiesReader.if_save_running_time() is False, reason="Ignore test to save time running")
@pytest.mark.order(5)
class TestAddToCardAFewItems(TestCaseBase):

    def setup_method(self):
        self.driver = self.get_driver()
        self.page = self.get_pages_model().get_inventory_page()
        self.page_inventory = self.page.get_inventory_section()
        self.page_header = self.page.get_header_section()

    def test_add_to_card_items(self):
        items = self.page_inventory.get_card_item_elements()
        for item in items: item.add_card.click()

        assert len(items) == self.page_header.get_amount_of_selceted_items()
