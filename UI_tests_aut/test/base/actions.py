from selenium.webdriver.android.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.action_chains import ActionChains


class BrowserActions():

    def __init__(self, driver: WebDriver) -> None:
        super().__init__()
        self.driver = driver
        self.actions = ActionChains(self.driver)

    def scrollToElement(self, element: WebElement):
        self.actions.move_to_element(element).perform()
