from seleniumpagefactory import PageFactory
from selenium import webdriver

from page_models.page_models_factory.pages.inventory_page.sections.footer_section import FooterSection
from page_models.page_models_factory.pages.inventory_page.sections.header_section import HeaderSection
from page_models.page_models_factory.pages.inventory_page.sections.inventory_section import InventorySection


class InventoryPageModel:

    def __init__(self, driver):
        self.inventory_section = None
        self.header_section = None
        self.footer_section = None
        self.driver = driver

    # locators = {
    #     "product": ('ID', 'item_4_title_link'),
    #
    # }

    def get_page_url(self) -> str:
        return 'https://www.saucedemo.com/inventory.html'

    def get_inventory_section(self) -> InventorySection:
        if self.inventory_section is None:
            self.inventory_section = InventorySection(self.driver)

        return self.inventory_section

    def get_header_section(self) -> HeaderSection:
        if self.header_section is None:
            self.header_section = HeaderSection(self.driver)

        return self.header_section

    def get_footer_section(self) -> FooterSection:
        if self.footer_section is None:
            self.footer_section = FooterSection(self.driver)

        return self.footer_section
