from enum import Enum

from selenium.webdriver.support.select import Select
from seleniumpagefactory import PageFactory

from UI_tests_aut.main.wait_factory.explicit_wait_factory import WaitFactory
from UI_tests_aut.main.page_models.page_models_factory.pages.inventory_page.sections.interfaces.filtering_data import FilteringMethod


class FilterValueEnum(Enum):
    NAME_ASC = "Name (A to Z)"
    NAME_DESC = "Name (Z to A)"
    PRICE_ASC = "Price (low to high)"
    PRICE_DESC = "Price (high to low)"


class HeaderSection(PageFactory, FilteringMethod):

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
        "filter_select": ('CSS', '#inventory_filter_container select'),
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

    def select_filter(self, value: FilterValueEnum):
        WaitFactory.wait_until_visibility_of_element(self.driver, self.filter_select)
        select = Select(self.filter_select)
        select.select_by_visible_text(value)
