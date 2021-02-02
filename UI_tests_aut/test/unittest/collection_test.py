from collections import namedtuple
import pytest
from pytest import approx


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

        assert global_variable == "global variable"

    def test_global_variable_access(self):
        assert global_variable == "global variable"

    def test_deleted_global_variable_access(self):
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

    def test_strings_id(self):
        x = "StringWith\nSpecificSymbol"
        y = r"StringWith\nSpecificSymbol"
        print(f'\n length x {len(x)} and length y {len(y)}')
        assert len(x) != len(y)

    def test_typing(self):
        x: list[str] = ["String", 0, True]
        assert type(x) != list[str]

    def test_slicing(self):
        x: list[str] = ["String", "String", "String"]
        y = 'It is simple string'
        z = 'y'

        print(y.find('a'))
        print(y.index('i'))
        print(z.isidentifier())
        assert "String" in x

    def test_numeric_types(self):
        x = 1.2 - 1.0
        y = float(-11)
        assert x == approx(0.2)

    def test_tuples(self):
        # Tuples are unchangeable. It is some possible to edit tuples using lists.

        tuples = (1, 2, 3, 4, 5)
        x_list = list(tuples)
        x_list.append(6)
        x_tuple = tuple(x_list)

        assert 6 in x_tuple

    def test_tuples_unpack(self):
        # Tuples are unchangeable. It is some possible to edit tuples using lists.

        tuples = (1, 2, 3, 4, 5)
        x, y, *z = tuples

        assert 5 in z
        assert isinstance(z, list)

    def test_tuples_for_loop(self):
        # Tuples are unchangeable. It is some possible to edit tuples using lists.

        tuples = ('One', 'Two', 'Three')

        for i in range(len(tuples)):
            print(f'Index is {i} . Value is: {tuples[i]}')

        tuples = tuples * 2
        assert len(tuples) == 6
        assert tuples.count('One') == 2

    def test_list(self):
        x_list = [1, 2, 3, 4, 5]
        x_list[0:2] = [0, 0]
        [print('\n' + str(x)) for x in x_list]

        assert x_list.count(0) == 2

    def test_list_comprehansion(self):
        x_list = [1, 2, 3, 4, 5]
        y_list = [x for x in x_list if x > 2]
        print(y_list)
        assert 2 not in y_list

    def test_list_sorting(self):
        x_list = [4, 5, -11, -4, 5]
        x_list.sort(reverse=True)
        y_list = [abs(x) for x in x_list if x < 0]
        z_list = x_list
        x_list.reverse()

        print(y_list)
        print(x_list)
        print(z_list)

    def test_name_tuples(self):
        Fruit = namedtuple('Fruit', ['name', 'price'])
        fruit_class = Fruit('orange', 11)

        print(fruit_class.price)
        print(fruit_class._fields)

    def test_dict_collection(self):
        my_dictionary = {
            'name': 'Full Name',
            'age': 16,
            'ifAdult': False
        }
        tuple = my_dictionary.items()
        print(my_dictionary.values())
        print(my_dictionary.keys())
        print(my_dictionary['name'])
        print(my_dictionary.get('name'))
        for x in tuple:
            print(f'Key is {x[0]}. Value is : {x[1]}')

        my_dictionary.update({'name': 'Surname'})
        print(my_dictionary)
        my_dictionary.update({'color': 'white'})
        print(my_dictionary)
        my_dictionary.pop('color')
        print(my_dictionary)
        my_dictionary.popitem()
        print(my_dictionary)
        for x in my_dictionary:
            print(x, my_dictionary[x])

        for x in my_dictionary.values():
            print(x)

    def test_sets_collection(self):

        my_set = {'name', 'surname', 'xx'}
        tropical = {"pineapple", "mango", "papaya", 'xx'}
        print(type(my_set))
        my_set.add('zz')
        print(my_set)
        my_set.update(tropical)
        print(my_set)
        my_set.remove("xx")
        my_set.discard("zxc")
        print(my_set)
        x = my_set.intersection(tropical)
        print(x)
