from project.product import Product

class Beverage(Product):
    def __init__(self, name, price, milliliters):
        super().__init__(name, price)
        self.__milliters = milliliters

    @property
    def milliliters(self):
        return self.__milliters