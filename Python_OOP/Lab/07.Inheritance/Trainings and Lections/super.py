"""
'self' - means this instance
'super()' - means this instance as  'Parent' class
    - Call it when in the same method (98% of the time)

"""

class Person: # 'Person' is extended by 'Teacher'
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f'Name: {self.name}; Age: {self.age}'

class Teacher(Person): # 'Teacher' extends 'Person'
    def teach(self):
        print(f'mr. {self.name} is teaching') # mr. Doncho is teaching

    def __str__(self):
        return f'{super().__str__()}; Subject: Python OOP'

    def __str__(self):
        parent_str = super().__str__()
        return f'{parent_str}; Subject: Python OOP'

t = Teacher('Doncho', 47)

print(t.name) # Doncho
print(t.age)  # 47
t.teach()
print(t)
