from shop import Shop
class ComputersShop(Shop):
    def __init__(self, number, name, product, unit, price, date, frequency, ram):
        super().__init__(number, name, product, unit, price, date)
        self.frequency = frequency
        self.ram       = ram
