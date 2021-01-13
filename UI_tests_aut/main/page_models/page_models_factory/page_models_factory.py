from selenium.webdriver.remote.webdriver import WebDriver

from UI_tests_aut.main.page_models.page_models_factory.pages.inventory_page.inventory_page import InventoryPageModel
from UI_tests_aut.main.page_models.page_models_factory.pages.login_page.login_page import LoginPageModel


class PageModelsFactory:
    def __init__(self, driver):
        super().__init__()
        self.driver = driver

    LOGIN_PAGE = None
    INVENTORY_PAGE = None

    def get_login_page(self) -> LoginPageModel:
        if self.LOGIN_PAGE is None:
            self.LOGIN_PAGE = LoginPageModel(self.driver)
        return self.LOGIN_PAGE

    def get_inventory_page(self) -> InventoryPageModel:
        if self.INVENTORY_PAGE is None:
            self.INVENTORY_PAGE = InventoryPageModel(self.driver)
        return self.INVENTORY_PAGE

