import pytest


@pytest.mark.collectionsTest
class TestCollection2InPython:

    def test_object_id(self):
        print('global_variable' in globals())
        print(dir(self))
