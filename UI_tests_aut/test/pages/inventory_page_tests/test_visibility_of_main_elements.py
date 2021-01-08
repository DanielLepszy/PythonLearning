from delayed_assert import expect, delayed_assert
from test.base.test_case_base import TestCaseBase


# @pytest.mark.order(5)
class TestInventoryPageLayout(TestCaseBase):

    def setup_method(self):
        self.driver = self.get_driver()
        self.page = self.get_pages_model().get_inventory_page()
        self.page_header = self.page.get_header_section()
        self.page_inventory = self.page.get_inventory_section()
        self.page_footer = self.page.get_footer_section()

    @delayed_assert.assert_all()
    def test_footer_section(self):
        for el in self.page_footer.get_footer_elements(): expect(el.is_displayed())


    @delayed_assert.assert_all()
    def test_inventory_section(self):
        card_models = self.page_inventory.get_card_item_elements()
        if len(card_models) == 6:
            for card in card_models:
                expect(card.image.is_displayed())
                expect(card.price.is_displayed())
                expect(card.add_card.is_displayed())
        else:
            raise Exception

    @delayed_assert.assert_all()
    def test_header_section(self):
        '''Headers logo'''
        expect(self.page_header.shopping_trolley_icon.is_displayed())
        expect(self.page_header.app_logo.is_displayed())
        expect(self.page_header.product_label.text == 'Products')

        '''Sidebars elements'''
        self.page_header.menu_burger_button.click()
        self.header_elements = self.page_header.get_sidebars_elements()
        expect(len(self.header_elements) is 4)
        for el in self.header_elements: expect(el.is_displayed())