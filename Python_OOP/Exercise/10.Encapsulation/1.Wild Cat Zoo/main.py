"""
Test Code:
from project.caretaker import Caretaker
from project.cheetah import Cheetah
from project.keeper import Keeper
from project.lion import Lion
from project.tiger import Tiger
from project.vet import Vet
from project.zoo import Zoo


zoo = Zoo("Zootopia", 3000, 5, 8)

# Animals creation
animals = [Cheetah("Cheeto", "Male", 2), Cheetah("Cheetia", "Female", 1), Lion("Simba", "Male", 4), Tiger("Zuba", "Male", 3), Tiger("Tigeria", "Female", 1), Lion("Nala", "Female", 4)]

# Animal prices
prices = [200, 190, 204, 156, 211, 140]

# Workers creation
workers = [Keeper("John", 26, 100), Keeper("Adam", 29, 80), Keeper("Anna", 31, 95), Caretaker("Bill", 21, 68), Caretaker("Marie", 32, 105), Caretaker("Stacy", 35, 140), Vet("Peter", 40, 300), Vet("Kasey", 37, 280), Vet("Sam", 29, 220)]

# Adding all animals
for i in range(len(animals)):
    animal = animals[i]
    price = prices[i]
    print(zoo.add_animal(animal, price))

# Adding all workers
for worker in workers:
    print(zoo.hire_worker(worker))

# Tending animals
print(zoo.tend_animals())

# Paying keepers
print(zoo.pay_workers())

# Fireing worker
print(zoo.fire_worker("Adam"))

# Printing statuses
print(zoo.animals_status())
print(zoo.workers_status())


output:

Cheeto the Cheetah added to the zoo
Cheetia the Cheetah added to the zoo
Simba the Lion added to the zoo
Zuba the Tiger added to the zoo
Tigeria the Tiger added to the zoo
Not enough space for animal
John the Keeper hired successfully
Adam the Keeper hired successfully
Anna the Keeper hired successfully
Bill the Caretaker hired successfully
Marie the Caretaker hired successfully
Stacy the Caretaker hired successfully
Peter the Vet hired successfully
Kasey the Vet hired successfully
Not enough space for worker
You tended all the animals. They are happy. Budget left: 1779
You payed your workers. They are happy. Budget left: 611
Adam fired successfully
You have 5 animals
----- 1 Lions:
Name: Simba, Age: 4, Gender: Male
----- 2 Tigers:
Name: Zuba, Age: 3, Gender: Male
Name: Tigeria, Age: 1, Gender: Female
----- 2 Cheetahs:
Name: Cheeto, Age: 2, Gender: Male
Name: Cheetia, Age: 1, Gender: Female
You have 7 workers
----- 2 Keepers:
Name: John, Age: 26, Salary: 100
Name: Anna, Age: 31, Salary: 95
----- 3 Caretakers:
Name: Bill, Age: 21, Salary: 68
Name: Marie, Age: 32, Salary: 105
Name: Stacy, Age: 35, Salary: 140
----- 2 Vets:
Name: Peter, Age: 40, Salary: 300
Name: Kasey, Age: 37, Salary: 280



"""


from project.caretaker import Caretaker
from project.cheetah import Cheetah
from project.keeper import Keeper
from project.lion import Lion
from project.tiger import Tiger
from project.vet import Vet
from project.zoo import Zoo



zoo = Zoo("Zootopia", 3000, 5, 8)

# Animals creation
animals = [Cheetah("Cheeto", "Male", 2), Cheetah("Cheetia", "Female", 1), Lion("Simba", "Male", 4), Tiger("Zuba", "Male", 3), Tiger("Tigeria", "Female", 1), Lion("Nala", "Female", 4)]

# Animal prices
prices = [200, 190, 204, 156, 211, 140]

# Workers creation
workers = [Keeper("John", 26, 100), Keeper("Adam", 29, 80), Keeper("Anna", 31, 95), Caretaker("Bill", 21, 68), Caretaker("Marie", 32, 105), Caretaker("Stacy", 35, 140), Vet("Peter", 40, 300), Vet("Kasey", 37, 280), Vet("Sam", 29, 220)]

# Adding all animals
for i in range(len(animals)):
    animal = animals[i]
    price = prices[i]
    print(zoo.add_animal(animal, price))

# Adding all workers
for worker in workers:
    print(zoo.hire_worker(worker))

    # Tending animals
print(zoo.tend_animals())

# Paying keepers
print(zoo.pay_workers())

# Fireing worker
print(zoo.fire_worker("Adam"))

# Printing statuses
print(zoo.animals_status())
print(zoo.workers_status())
