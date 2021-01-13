from selenium.webdriver.common.by import By
from seleniumpagefactory import PageFactory
from selenium import webdriver

from UI_tests_aut.main.wait_factory.explicit_wait_factory import WaitFactory


class HeaderSection(PageFactory):

    def __init__(self, driver):
        super().__init__()
        self.driver = driver

    locators = {
        "shopping_trolley_icon": ('CSS', '#shopping_cart_container .fa-fw'),
        "shopping_counter": ('CSS', '#shopping_cart_container .shopping_cart_badge'),
        "app_logo": ('CSS', '.app_logo'),
        "product_label": ('CSS', '#inventory_filter_container .product_label'),
        "menu_burger_button": ('CSS', '#menu_button_container .bm-burger-button'),
        "all_items_sidebar": ('ID', 'inventory_sidebar_link'),
        "about_sidebar": ('ID', 'about_sidebar_link'),
        "logout_sidebar": ('ID', 'logout_sidebar_link'),
        "cross_sidebar_button": ('CSS', '.bm-cross-button button'),
    }

    def logout_from_app(self):
        # WaitFactory.wait_until_element_presence(self.driver, '#menu_button_container .bm-burger-button')
        # self.driver.find_element_by_css_selector('#menu_button_container .bm-burger-button').click()
        self.menu_burger_button.click()
        WaitFactory.wait_until_visibility_of_element(self.driver, self.logout_sidebar)
        self.logout_sidebar.click()

    def get_sidebars_elements(self) -> list:
        return self.driver.find_elements_by_xpath('//nav/descendant::a')

    def get_amount_of_selceted_items(self):
        WaitFactory.wait_until_visibility_of_element(self.driver, self.shopping_counter)
        # shopping_counter = self.driver.find_element_by_css_selector('#shopping_cart_container .shopping_cart_badge')
        return int(self.shopping_counter.text)
