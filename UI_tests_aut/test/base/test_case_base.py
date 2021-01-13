from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.support.event_firing_webdriver import EventFiringWebDriver

from UI_tests_aut.main.browsers_model.browsers import Browsers
from UI_tests_aut.main.page_models.page_models_factory.page_models_factory import PageModelsFactory
from UI_tests_aut.main.properties.read_properties import PropertiesReader
from UI_tests_aut.test.base.actions import BrowserActions


class TestCaseBase:
    DRIVER:WebDriver = None
    PAGES = None
    ACTIONS: BrowserActions = None

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

    @classmethod
    def get_actions(cls) -> BrowserActions:
        if TestCaseBase.ACTIONS is not None:
           return TestCaseBase.ACTIONS
        else:
            TestCaseBase.ACTIONS = BrowserActions(TestCaseBase.DRIVER)
            return TestCaseBase.ACTIONS
