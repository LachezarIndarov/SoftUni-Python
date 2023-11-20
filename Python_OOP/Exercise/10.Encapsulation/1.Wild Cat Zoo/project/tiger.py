from project.animal import Animal

class Tiger(Animal):
    Money_FOR_CARE = 45

    def __init__(self, name, gender, age):
        super().__init__(name, gender, age, self.Money_FOR_CARE)