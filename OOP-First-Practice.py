#Instantiate my class
class Item:
    pay_rate = 0.8 #The pay rate after 20% discount
    all = []
    def __init__(self, name: str, price: float, quantity=0):
        #Validate my code to only accept from the correc interegers
        assert quantity >= 0
        assert price >= 0,  f"The Price: {price}, is less than 1"
        assert quantity >= 0, f"The Quantity: {quantity}, is less than 1"

        #assigning self objects
        self.name = name
        self.price = price
        self.quantity = quantity

        #actions to execute
        Item.all.append(self)

    def calculate_total_prices(self):
        return self.price * self.quantity
    
    def apply_discount(self):
        self.price = self.price * self.pay_rate
    
    def __repr__(self):
        pass

item1 = Item('Phone', 100, 1)
item2 = Item('Laptop', 1000, 3)
item3 = Item('Cable', 10, 5)
item4 = Item('Mouse', 50, 5)
item5 = Item('Keyboard', 75, 5)

for instance in Item.all:
    print(instance.name)