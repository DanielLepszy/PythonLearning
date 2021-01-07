from selenium.webdriver.firefox.webdriver import WebDriver

from browsers_model.browsers import Browsers
from properties.read_properties import PropertiesReader
from page_models import PageModelsFactory


class TestCaseBase:
    DRIVER = None
    PAGES = None

    @classmethod
    def set_driver(cls) -> WebDriver:
        cls.DRIVER = Browsers(PropertiesReader().load_properties_from_file('browser_type').data).driver
        return cls.DRIVER

    @classmethod
    def get_pages_model(cls) -> PageModelsFactory:
        if cls.PAGES is None:
            cls.PAGES = PageModelsFactory(cls.DRIVER)
        return cls.PAGES

    @classmethod
    def get_driver(cls) -> WebDriver:
        if cls.DRIVER is not None:
            return TestCaseBase.DRIVER
        else:
            return TestCaseBase.set_driver()
