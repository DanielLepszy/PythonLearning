import pytest


@pytest.mark.filteringTest
class TestFilterMethods:
    items_name = ["Sauce Labs Backpack", "Sauce Labs Bike Light", "Sauce Labs Bolt T-Shirt", "Sauce Labs Fleece Jacket",
                  "Sauce Labs Onesie", "Test.allTheThings() T-Shirt (Red)"]

    items_price = [15.99, 7.99, 49.99, 15.99, 9.99, 29.99]

    def test_filtering_ascending_items_name(self):
        self.items_name.sort()
        sorted_tuple = tuple(self.items_name)
        assert type(sorted_tuple) is tuple

    def test_filtering_descending_items_name(self):
        self.items_name.sort(reverse=True)
        sorted_tuple = tuple(self.items_name)
        assert type(sorted_tuple) is tuple

    def test_filtering_ascending_items_price(self):
        self.items_price.sort()
        sorted_tuple = tuple(self.items_price)
        assert sorted_tuple[0] == 7.99

    def test_filtering_descending_items_price(self):
        self.items_price.sort(reverse=True)
        sorted_tuple = tuple(self.items_price)
        assert sorted_tuple[0] == 49.99
