from seleniumpagefactory import PageFactory
from selenium import webdriver

class LoginPageModel(PageFactory):

    def __init__(self, driver):
        super().__init__()
        self.driver = driver
        # self.highlight = True

    locators = {
        "username_input": ('ID', 'user-name'),
        "password_input": ('ID', 'password'),
        "login_button": ('ID', 'login-button'),
        "error_header": ('CSS', 'h3[data-test="error"]'),
    }

    def set_credentials_to_inputs(self, username, password):
        self.username_input.send_keys(username)
        self.password_input.send_keys(password)
        self.login_button.click()
