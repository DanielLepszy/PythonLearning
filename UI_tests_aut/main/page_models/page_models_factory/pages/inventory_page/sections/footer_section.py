from selenium.webdriver.remote.webelement import WebElement
from seleniumpagefactory import PageFactory
from selenium import webdriver


class FooterSection(PageFactory):

    def __init__(self, driver):
        super().__init__()
        self.driver = driver

    locators = {
        "social_twitter": ('CSS', '.footer .social_twitter'),
        "social_facebook": ('CSS', '.footer .social_facebook'),
        "social_linkedin": ('CSS', '.footer .social_linkedin'),
        "footer_copy": ('CSS', '.footer .footer_copy'),
        "footer_robot": ('CSS', '.footer .footer_robot'),

    }

    def get_footer_elements(self) -> list[WebElement]:
        elements = [self.social_twitter, self.social_facebook, self.social_linkedin, self.footer_copy,
                    self.footer_robot]
        return elements
