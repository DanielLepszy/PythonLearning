from seleniumpagefactory import PageFactory
from selenium import webdriver


class InventorySection(PageFactory):

    def __init__(self, driver):
        super().__init__()
        self.driver = driver


locators = {
    "label": ('CSS', '#inventory_filter_container .product_label'),

}
