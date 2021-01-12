from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class WaitFactory:
    driver = None
    time = 5

    @staticmethod
    def wait_until_element_presence(driver, locator):
        WebDriverWait(driver, WaitFactory.time).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, locator))
        )

    @staticmethod
    def wait_until_element_visible(driver, locator):
        WebDriverWait(driver, WaitFactory.time).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, locator))
        )

    # @staticmethod
    # def wait_until_element_invisible(driver, locator):
    #     WebDriverWait(driver, WaitFactory.time).until(
    #         EC.invisibility_of_element_located((By.CSS_SELECTOR, locator))
    #     )

    @staticmethod
    def wait_until_element_invisible(driver, by: By, locator):
        WebDriverWait(driver, WaitFactory.time).until(
            EC.invisibility_of_element_located((by, locator))
        )

    @staticmethod
    def wait_until_text_to_be_present(driver, locator, text):
        WebDriverWait(driver, WaitFactory.time).until(
            EC.text_to_be_present_in_element((By.CSS_SELECTOR(locator), text), "No data to display")
        )

    @staticmethod
    def wait_until_visibility_of_all_elements(driver, locator):
        WebDriverWait(driver, WaitFactory.time).until(
            EC.visibility_of_all_elements_located((By.XPATH, locator))
        )

    @staticmethod
    def wait_until_visibility_of_element(driver, element):
        WebDriverWait(driver, WaitFactory.time).until(
            EC.visibility_of(element)
        )

    @staticmethod
    def wait_until_element_to_be_clickable(driver, By: By, locator):
        WebDriverWait(driver, WaitFactory.time).until(
            EC.element_to_be_clickable((By, locator))
        )
