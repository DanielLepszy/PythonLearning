from seleniumpagefactory import PageFactory
from selenium import webdriver

from wait_factory.explicit_wait_factory import WaitFactory


class HeaderSection(PageFactory):

    def __init__(self, driver):
        super().__init__()
        self.driver = driver

    locators = {
        "shopping_trolley_icon": ('CSS', '#shopping_cart_container .fa-fw'),
        "menu_burger_button": ('CSS', '#menu_button_container .bm-burger-button'),
        "all_items_sidebar": ('ID', 'inventory_sidebar_link'),
        "about_sidebar": ('ID', 'about_sidebar_link'),
        "logout_sidebar": ('ID', 'logout_sidebar_link'),

    }

    def logout_from_app(self):
        self.menu_burger_button.click()
        WaitFactory.wait_until_visibility_of_element(self.driver, self.logout_sidebar)
        self.logout_sidebar.click()
