#Instantiate my class
class Item:
    def __init__(self, name, price, quantity):
        print(f'Instance has been created for: {name}')
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_total_prices(self, x, y):
        return x * y
    pass

item1 = Item('Laptop', 2000, 2)

item2 = Item('Phone', 200, 3)


print (item1.name)
print (item2.name)