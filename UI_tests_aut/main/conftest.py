import sys

import pytest

saveTime = pytest.mark.skipif(reason="block tests to save execution time")

@pytest.fixture
def input_value():
   input = 39
   return input