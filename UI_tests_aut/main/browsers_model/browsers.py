from selenium import webdriver
from selenium.webdriver.support.event_firing_webdriver import EventFiringWebDriver
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.utils import ChromeType

from UI_tests_aut.main.browsers_model.chrome_browser import Chrome
from UI_tests_aut.main.browsers_model.firefox_browser import Firefox


class Browsers(Firefox, Chrome):

    def __init__(self, browser_type):
        super().__init__()
        self.driver = self.set_driver(browser_type)

    # def get_driver(self):
    #     if self.driver is not None:
    #         return self.driver

    def set_driver(self, browser_type) -> webdriver:
        if browser_type == Firefox().get_browser_type():
            # return EventFiringWebDriver(drv, Listeners())
            return webdriver.Firefox(executable_path=GeckoDriverManager().install())

            # , log_path='../main/browsers_model/driver_log/gecko_driver.log')
        elif browser_type == Chrome().get_browser_type():
            # return EventFiringWebDriver(drv, Listeners())
            return webdriver.Chrome(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install())
        else:
            raise Exception(f'Wrong browser_type:{browser_type}')
