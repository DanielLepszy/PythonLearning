from seleniumpagefactory import PageFactory
from selenium import webdriver


class HeaderSection(PageFactory):

    def __init__(self, driver):
        super().__init__()
        self.driver = driver


    locators = {
        "username_input": ('ID', 'user-name'),

    }
