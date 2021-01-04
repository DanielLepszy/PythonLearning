# from UI_tests_aut.main.browsers_model.chrome_browser import Chrome
# from UI_tests_aut.main.browsers_model.browsers import Browsers
# from UI_tests_aut.main.browsers_model.firefox_browser import Firefox
# from UI_tests_aut.main.properties.read_properties import Properties_Reader
# import pytest
#
#
# @pytest.mark.order(2)
# class Test_Login_With_No_Credential:
#
#
#     def setup_class(self):
#         self.driver = Browsers.get_driver()
#         self.driver.get(Properties_Reader().load_properties_from_file('url').data)
#
#     @pytest.fixture()
#     def prepare_elements(self):
#         self.username_input = self.driver.find_element_by_id('user-name')
#         self.password_input = self.driver.find_element_by_id('password')
#         self.login_button = self.driver.find_element_by_id('login-button')
#         self.error_header_css = 'h3[data-test="error"]'
#
#     def test_validation_input(self, prepare_elements):
#         self.username_input.send_keys('username_test')
#         self.password_input.send_keys('password_test')
#         self.login_button.click()
#         self.error_validation_message = self.driver.find_element_by_css_selector(self.error_header_css).text
#
#         assert self.error_validation_message == 'Epic sadface: Username and password do not match any user in this service'
#
