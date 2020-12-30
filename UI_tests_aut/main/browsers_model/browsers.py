from selenium import webdriver;
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.chrome import ChromeDriverManager

class Browsers:

    def __init__(self, browser_type):
        self.set_driver(browser_type)

    def get_driver(self):
        return self.driver

    def set_driver(self, browser_type):
        if browser_type == 'firefox':
            self.driver = webdriver.Firefox(executable_path=GeckoDriverManager().install(), log_path='../main/browsers_model/driver_log/gecko_driver.log')
        elif browser_type == 'chrome':
            self.driver = webdriver.Chrome(executable_path=ChromeDriverManager.install(), log_path='../main/browsers_model/driver_log/chrome_driver.log')
        else:
            raise Exception(f'Wrong browser_type:{browser_type}')



