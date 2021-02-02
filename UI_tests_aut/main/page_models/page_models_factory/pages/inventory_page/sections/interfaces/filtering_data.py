class FilteringMethod:

    def filtering_ascending_items_name(self, items_name: list[str]):
        items_name.sort()
        sorted_tuple = tuple(items_name)
        assert type(sorted_tuple) is tuple

    def filtering_descending_items_name(self,items_name: list[str]):
        items_name.sort(reverse=True)
        sorted_tuple = tuple(items_name)
        assert type(sorted_tuple) is tuple

    def filtering_ascending_items_price(self,items_price: list[float]):
        items_price.sort()
        sorted_tuple = tuple(items_price)
        assert sorted_tuple[0] == 7.99

    def filtering_descending_items_price(self,items_price: list[float]):
        items_price.sort(reverse=True)
        sorted_tuple = tuple(items_price)
        assert sorted_tuple[0] == 49.99
