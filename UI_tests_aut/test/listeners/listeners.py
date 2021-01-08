from selenium.webdriver.support.abstract_event_listener import AbstractEventListener


class Listeners(AbstractEventListener):

    def on_exception(self, exception, driver):
        print("-----------")