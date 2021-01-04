import pytest

from browsers_model.browsers import Browsers
from properties.read_properties import Properties_Reader


class Test_Case_Base:

    driver = None

    @classmethod
    def set_driver(cls):
        cls.driver = Browsers(Properties_Reader().load_properties_from_file('browser_type').data).driver
        Test_Case_Base.driver = cls.driver
        return cls.driver

    @staticmethod
    def get_driver():
        return Test_Case_Base.driver


