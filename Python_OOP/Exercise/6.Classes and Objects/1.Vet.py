"""
Test Code:
peter = Vet("Peter")
george = Vet("George")
print(peter.register_animal("Tom"))
print(george.register_animal("Cory"))
print(peter.register_animal("Fishy"))
print(peter.register_animal("Bobby"))
print(george.register_animal("Kay"))
print(george.unregister_animal("Cory"))
print(peter.register_animal("Silky"))
print(peter.unregister_animal("Molly"))
print(peter.unregister_animal("Tom"))
print(peter.info())
print(george.info())

output
Tom registered in the clinic
Cory registered in the clinic
Fishy registered in the clinic
Bobby registered in the clinic
Kay registered in the clinic
Cory unregistered successfully
Silky registered in the clinic
Molly not in the clinic
Tom unregistered successfully
Peter has 3 animals. 1 space left in clinic
George has 1 animals. 1 space left in clinic



"""
class Vet:
    animals = []
    space = 5

    def __init__(self,name):
        self.name = name
        self.animals = []

    def register_animal(self, animal_name):
        print(self.space)

        if len(Vet.animals) >= Vet.space:
            return 'Not enough space'
        self.animals.append(animal_name)
        Vet.animals.append(animal_name)
        return f"{animal_name} registered in the clinic"


    def unregister_animal(self, animal_name):
        if animal_name not in self.animals:
            return f"{animal_name} not in the clinic"
        self.animals.remove(animal_name)
        Vet.animals.remove(animal_name)
        return f"{animal_name} unregistered successfully"

    def info(self):
        return f"{self.name} has {len(self.animals)} animals. {Vet.space - Vet.animals} space left in clinic"






