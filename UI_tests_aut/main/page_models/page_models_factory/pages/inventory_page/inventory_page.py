from seleniumpagefactory import PageFactory
from selenium import webdriver

from page_models.page_models_factory.pages.inventory_page.sections.inventory_section import InventorySection


class InventoryPageModel(PageFactory, InventorySection):

    def __init__(self, driver):
        super().__init__()
        self.driver = driver

    locators = {
        "product": ('ID', 'item_4_title_link'),

    }

    def get_page_url(self) -> str:
        return 'https://www.saucedemo.com/inventory.html'
