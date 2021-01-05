from browsers_model.browsers import Browsers
from properties.read_properties import PropertiesReader
from page_models.page_models_factory.page_models_factory import PageModelsFactory


class TestCaseBase:

    DRIVER = None
    PAGES = None

    @classmethod
    def set_driver(cls):
        cls.DRIVER = Browsers(PropertiesReader().load_properties_from_file('browser_type').data).driver
        return cls.DRIVER

    @classmethod
    def get_pages_model(cls):
        if cls.PAGES is None:
            cls.PAGES = PageModelsFactory(cls.DRIVER)
        return cls.PAGES

    @classmethod
    def get_driver(cls):
        if cls.DRIVER is not None:
            return TestCaseBase.DRIVER
        else:
            TestCaseBase.set_driver()


