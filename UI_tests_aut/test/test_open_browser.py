import pytest
from UI_tests_aut.main.properties.read_properties import Properties_Reader
from test.test_case_base import Test_Case_Base


@pytest.mark.order(1)
class TestClass(Test_Case_Base):

    def setup_class(self):
        self.driver = Test_Case_Base.set_driver()
        self.url = Properties_Reader().load_properties_from_file('url').data

    def test_open(self):
        # self.driver.implicitly_wait(3)
        self.driver.get(self.url)
        assert self.driver.current_url == 'https://www.saucedemo.com/'
