"""
Test Code:
cup = Cup(100, 50)
print(cup.status())
cup.fill(40)
cup.fill(20)
print(cup.status())

output1
50
10

"""
class Cup:
    def __init__(self, size, quantity):

        self.size = size
        self.quantity = quantity

    def status(self):
        return self.size - self.quantity

    def fill(self,mililiters):
        if self.status() >= mililiters:
            self.quantity += mililiters


cup = Cup(100, 50)
print(cup.status())
cup.fill(40)
cup.fill(20)
print(cup.status())