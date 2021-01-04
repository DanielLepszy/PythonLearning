import unittest

import capybara as capybara

from browsers_model.browsers import Browsers
from properties.read_properties import Properties_Reader


class Test_Case_Base(unittest.TestCase):

    @capybara.register_driver("selenium")
    @classmethod
    def setup_class(cls):
        Browsers(Properties_Reader().load_properties_from_file('browser_type').data)
        cls.driver = Browsers.get_driver()

    def setUp(self):
        Browsers(Properties_Reader().load_properties_from_file('browser_type').data)
        self.driver = Browsers.get_driver()

    def tearDown(self):
        self.driver.get("about:blank")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()