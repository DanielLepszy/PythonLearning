import pytest
from selenium.webdriver.android.webdriver import WebDriver
from selenium.webdriver.support.abstract_event_listener import AbstractEventListener

from properties.read_properties import PropertiesReader
from test.base.test_case_base import TestCaseBase


class Listeners(AbstractEventListener):

    def on_exception(self, exception, driver):
        print('---------------------------------')


# @pytest.mark.skipif(PropertiesReader.if_save_running_time(), reason="Ignore test to save time running")
@pytest.mark.order(1)
class TestClass(TestCaseBase):

    def setup_class(self):
        self.driver: WebDriver = self.get_driver()
        self.url = PropertiesReader().load_properties_from_file('url').data

    def test_open(self):
        ''' implicit wait for all web-elements'''
        self.driver.implicitly_wait(2)
        self.driver.get(self.url)
        # self.driver.get_screenshot_as_file('fullscreen.png')
        # im = ImageGrab.grab(bbox=(0, 0, 1800, 1064))
        # im.save("fullscreen.png")
        raise Exception
        # assert self.driver.current_url == 'https://www.saucedemo.com/'
