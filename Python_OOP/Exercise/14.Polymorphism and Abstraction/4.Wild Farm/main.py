"""
input1
owl = Owl("Pip", 10, 10)
print(owl)
meat = Meat(4)
print(owl.make_sound())
owl.feed(meat)
veg = Vegetable(1)
print(owl.feed(veg))
print(owl)

output1
Owl [Pip, 10, 10, 0]
Hoot Hoot
Owl does not eat Vegetable!
Owl [Pip, 10, 11.0, 4]


input2
hen = Hen("Harry", 10, 10)
veg = Vegetable(3)
fruit = Fruit(5)
meat = Meat(1)
print(hen)
print(hen.make_sound())
hen.feed(veg)
hen.feed(fruit)
hen.feed(meat)
print(hen)


output2
Hen [Harry, 10, 10, 0]
Cluck
Hen [Harry, 10, 13.15, 9]


"""
from project.animals.birds import Owl, Hen
from project.food import Meat, Vegetable, Fruit


owl = Owl("Pip", 10, 10)
print(owl)
meat = Meat(4)
print(owl.make_sound())
owl.feed(meat)
veg = Vegetable(1)
print(owl.feed(veg))
print(owl)


hen = Hen("Harry", 10, 10)
veg = Vegetable(3)
fruit = Fruit(5)
meat = Meat(1)
print(hen)
print(hen.make_sound())
hen.feed(veg)
hen.feed(fruit)
hen.feed(meat)
print(hen)

