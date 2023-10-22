class Shop:
    def __init__(self, name, items):
        self.name = name
        self.items = items

    def get_items_count(self):
        return len(self.items)


shop = Shop("My Shop", ["Apples", "Bananas", "Cucumbers", "Melon"])
shop2 = Shop('Jon', ['Lemons'])
print(shop.get_items_count())
print(shop2.get_items_count())
