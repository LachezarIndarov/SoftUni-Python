"""
Test Code:
mammal = Mammal("Dog", "Domestic", "Bark")
print(mammal.make_sound())
print(mammal.get_kingdom())
print(mammal.info())

output
Dog makes Bark
animals
Dog is of type Domestic

"""

class Mammal:

    # class atribute
    __kingdom = "animals"

    def __init__(self, name, type, sound):
        self.name = name
        self.type = type
        self.sound = sound

    # method
    def make_sound(self):
        return f"{self.name} makes {self.sound}"
    # method
    def get_kingdom(self):
        return self.__kingdom
    # method
    def info(self):
        return f"{self.name} is of type {self.type}"


mammal = Mammal("Dog", "Domestic", "Bark")
print(mammal.make_sound())
print(mammal.get_kingdom())
print(mammal.info())
