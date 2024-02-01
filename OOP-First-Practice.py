#Instantiate my class
class Item:

    def __init__(self, name: str, price: float, quantity=0):
        #Validate my code to only accept from the correc interegers
        assert quantity >= 0
        assert price >= 0,  f"The Price: {price}, is less than 1"
        assert quantity >= 0, f"The Quantity: {quantity}, is less than 1"



        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_total_prices(self):
        return self.price * self.quantity
    

item1 = Item('Laptop', -2000, 2)

item2 = Item('Phone', -200, 3)

item2.has_numpad = False #Meaning you can add methods to classes even after.


print (item1.calculate_total_prices())
print (item2.calculate_total_prices())
