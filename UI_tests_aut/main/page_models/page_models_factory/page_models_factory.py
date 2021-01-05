from page_models.login_page import LoginPageModel


class PageModelsFactory:
    def __init__(self, driver) -> None:
        super().__init__()
        self.driver = driver

    LOGIN_PAGE = None

    def get_login_page(self):
        if self.LOGIN_PAGE is None:
            self.LOGIN_PAGE = LoginPageModel(self.driver)
        return self.LOGIN_PAGE
