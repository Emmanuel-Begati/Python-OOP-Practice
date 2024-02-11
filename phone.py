from item import Item

class Phone(Item):
    def __init__(self, name: str, price: float, quantity=0, broken_phones=0):
        assert broken_phones >= 0, f"The Quantity: {broken_phones}, is less than 1"
        
        super().__init__(name, price, quantity)
        self.broken_phones = broken_phones
        

phone1 = Phone('iPhone 12', 1000, 5, 1)
phone2 = Phone('Samsung S20', 900, 3, 2)
