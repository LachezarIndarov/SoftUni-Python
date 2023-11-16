from project.animal import Animal

class Lion(Animal):
    Money_FOR_CARE = 50

    def __init__(self, name, gender, age):
        super().__init__(name, gender, age, self.Money_FOR_CARE)
