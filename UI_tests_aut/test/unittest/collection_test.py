import pytest


@pytest.mark.collectionsTest
class TestCollectionInPython:

    def test_varibales_types(self):
        x, y, z = 'some_text', 1, True

        assert type(x) is str
        assert type(y) is int
        assert type(z) is bool

    def test_varibales_collection(self):
        many_types = ["apple", 2, True]
        x, y, z = many_types

        assert type(x) is str
        assert type(y) is int
        assert type(z) is bool

    def test_global_variable(self):
        global global_variable
        global_variable = "global variable"

        assert global_variable is "global variable"

    def test_global_variable_access(self):
        assert global_variable is "global variable"

    def test_deleted_global_variable_access(self):
        print(dir())
        del global_variable
        assert 'global_variable' in globals()

        ''' Comparison operator '''

    def test_comparison_operator(self):
        ''' identity operator : is/is not '''
        ''' equality operator : == / != '''
        list1 = [1, 2, 3]
        list2 = [1, 2, 3]
        list3 = list1

        assert list1 == list2
        assert list1 is not list2
        assert list3 is list1
        assert 3 in list1
        assert 333 not in list1

    def test_object_id(self):

        list1 = [1, 2, 3]
        list2 = [1, 2, 3]
        list3 = list1

        assert id(list2) is not id(list3)
        assert id(list2) != id(list3)
        assert id(list1) is not id(list3)
        assert id(list1) == id(list3)

