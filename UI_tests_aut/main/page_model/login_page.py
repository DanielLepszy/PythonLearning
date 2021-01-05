from seleniumpagefactory import PageFactory


class LoginPage(PageFactory):

    def __init__(self, driver):
        self.driver = driver
        self.timeout = 5
        self.highlight = True

    locators = {
        "username_input": ('ID', 'user-name'),
        "password_input": ('ID', 'password'),
        "login_button": ('ID', 'login-button'),

    }