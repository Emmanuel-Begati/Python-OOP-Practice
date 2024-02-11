import csv
#Instantiate my class
class Item:
    pay_rate = 0.8 #The pay rate after 20% discount
    all = []
    def __init__(self, name: str, price: float, quantity=0):
        #Validate my code to only accept from the correc interegers
        # assert quantity >= 0
        assert price >= 0,  f"The Price: {price}, is less than 1"
        assert quantity >= 0, f"The Quantity: {quantity}, is less than 1"

        #assigning self objects
        self._name = name
        self.price = price
        self.quantity = quantity

        #actions to execute
        Item.all.append(self)

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        self._name = value
     
    def calculate_total_prices(self):
        return self.price * self.quantity
    
    def apply_discount(self):
        self.price = self.price * self.pay_rate
        return self.price

    @classmethod
    def instantiate_from_csv(cls):
        with open('items.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)

        for item in items:
            Item(
                name=item.get('name'),
                price=float(item.get('price', 0.0)),
                quantity=int(item.get('quantity', 0))
            )
    
    @staticmethod
    def is_integer(num):
        #We will count out the float numbers that are point zero
       if isinstance(num, float):
           #Count out the float numbers that are point zero
           return num.is_integer()
       elif isinstance(num, int):
           return True
       else:
           return False

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})"
    
    