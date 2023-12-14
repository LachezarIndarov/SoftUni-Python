class Person:
    def __init__(self, name):
        self.name = name

    @staticmethod
    def is_adult(age):
        return age >= 18



print(Person.is_adult(5)) # False
girl = Person("Amy")
print(girl.is_adult(20))  # True

