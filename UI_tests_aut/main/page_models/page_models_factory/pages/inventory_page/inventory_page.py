from seleniumpagefactory import PageFactory
from selenium import webdriver


class InventoryPageModel(PageFactory):

    def __init__(self, driver):
        super().__init__()
        self.driver = driver


locators = {
    "username_input": ('ID', 'user-name'),
    "password_input": ('ID', 'password'),
    "login_button": ('ID', 'login-button'),
    "error_header": ('CSS', 'h3[data-test="error"]'),
}
