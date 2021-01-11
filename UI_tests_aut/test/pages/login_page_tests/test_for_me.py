# import unittest
# import logging
# from selenium import webdriver
# from selenium.webdriver import Firefox
# from selenium.webdriver.support.events import EventFiringWebDriver, AbstractEventListener
# from webdriver_manager.firefox import GeckoDriverManager
#
#
# class MyListener(AbstractEventListener):
#     def before_navigate_to(self, url, driver):
#         print("Before navigate to %s" % url)
#
#     def after_navigate_to(self, url, driver):
#         print("After navigate to %s" % url)
#
#     def on_exception(self, exception, driver):
#         print("on excpetion %s" % exception)
#
#
# class Test(unittest.TestCase):
#     def test_logging_file(self):
#         driver_plain = webdriver.Firefox(executable_path=GeckoDriverManager().install())
#         edriver = EventFiringWebDriver(driver_plain, MyListener())
#         edriver.get("https://google.com")
#         ee = edriver.find_element_by_css_selector('.asdad')
# #      ????????????//
#
