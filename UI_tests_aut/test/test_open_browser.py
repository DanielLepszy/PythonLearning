# from UI_tests_aut.main.browsers_model.firefox_browser import Firefox
# from UI_tests_aut.main.properties.read_properties import Properties_Reader
#
# class TestClass:
#
#     def setup_class(self):
#         self.driver = Firefox().get_driver()
#         self.url = Properties_Reader().load_properties_from_file('url').data
#
#     def test_open(self):
#         self.driver.get(self.url)
#         assert self.driver.current_url == self.url
#
#     def teardown_class(self):
#         self.driver.close()
