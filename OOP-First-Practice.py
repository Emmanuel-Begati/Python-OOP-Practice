#Instantiate my class
class Item():
    def calculate_total_prices(self, x, y):
        return x * y
    pass

item = Item()
item.name = 'Laptop'
item.price = 2000
item.quantity = 2
print(item.calculate_total_prices(item.price, item.quantity))

item2 = Item()
item2.name = 'Phone'
item2.price = 200
item2.quantity = 3
print(item2.calculate_total_prices(item2.price, item2.quantity))
