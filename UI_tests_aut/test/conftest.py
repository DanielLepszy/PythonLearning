import pytest

from properties.read_properties import Properties_Reader


@pytest.hookimpl()
def pytest_sessionstart(session):
    print("hello")
#
# @pytest.fixture(scope='class')
# def get_url(property):
#     return Properties_Reader().load_properties_from_file(property).data
