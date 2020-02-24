from shop import Shop
class AppliancesShop(Shop):
    def __init__(self, number, name, product, unit, price, date, domain, subdomain):
        super().__init__(number, name, product, unit, price, date)
        self.domain    = domain
        self.subdomain = subdomain
