from browsers_model.browsers import Browsers
from properties.read_properties import PropertiesReader


class TestCaseBase:

    DRIVER = None

    @classmethod
    def set_driver(cls):
        cls.driver = Browsers(PropertiesReader().load_properties_from_file('browser_type').data).driver
        TestCaseBase.DRIVER = cls.driver
        return cls.driver

    @staticmethod
    def get_driver():
        return TestCaseBase.DRIVER


