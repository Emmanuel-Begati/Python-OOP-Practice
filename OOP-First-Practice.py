#Instantiate my class
class Item:
    pay_rate = 0.8 #The pay rate after 20% discount
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
    
    def apply_discount(self):
        self.price = self.price * self.pay_rate
    

item = Item('Laptop', 2000, 2)

item.apply_discount()
print(item.price)
item.pay_rate = 0.7
item.apply_discount()
print(item.price)