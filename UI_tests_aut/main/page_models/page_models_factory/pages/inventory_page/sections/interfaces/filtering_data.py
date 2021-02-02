class FilteringMethod:

    def filtering_ascending_items_name(self, items_name: list[str]):
        items_name.sort()
        return tuple(items_name)

    def filtering_descending_items_name(self,items_name: list[str]):
        items_name.sort(reverse=True)
        return tuple(items_name)

    def filtering_ascending_items_price(self,items_price: list[float]):
        items_price.sort()
        return tuple(items_price)

    def filtering_descending_items_price(self,items_price: list[float]):
        items_price.sort(reverse=True)
        return tuple(items_price)
