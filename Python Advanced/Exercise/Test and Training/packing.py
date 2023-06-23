list1 = [1, 2, 3, 4]

k, l, *r = list1
print(k, l , r) # 1 2 [3, 4]

list2 = [-1, *list1, -2]
print(list2) # [-1, 1, 2, 3, 4, -2]

#-----------------------------------------
dicrionary1 = {

    'x': 1,
    'y': 2

}

dicrionary2 = {

    'z': 3,
    **dicrionary1,
}

print(dicrionary2) # {'z': 3, 'x': 1, 'y': 2}

#------------------------------------

def f(*args, **kwargs):
    print(f'*args = {args}, kwargs = {kwargs}')

numbers = [1, 2, 3, 4, 5]
grades_dict = {

    'Doncho': 3,
    'Ivan': 4,
    'Maria': 6,
    'Pesho': 4.5

}


f(numbers)               # *args = ([1, 2, 3, 4, 5],), kwargs = {}
f(grades_dict)           # *args = ({'Doncho': 3, 'Ivan': 4, 'Maria': 6, 'Pesho': 4.5},), kwargs = {}
f(numbers, grades_dict)  # *args = ([1, 2, 3, 4, 5], {'Doncho': 3, 'Ivan': 4, 'Maria': 6, 'Pesho': 4.5}), kwargs = {}


f(*numbers)                # *args = (1, 2, 3, 4, 5), kwargs = {}
f(**grades_dict)           # *args = (), kwargs = {'Doncho': 3, 'Ivan': 4, 'Maria': 6, 'Pesho': 4.5}
f(*numbers, **grades_dict) # *args = (1, 2, 3, 4, 5), kwargs = {'Doncho': 3, 'Ivan': 4, 'Maria': 6, 'Pesho': 4.5}

#----------------------------------------------------

def f(*args, **kwargs):
    print(f'*args = {args}, kwargs = {kwargs}')

def shame_doncho(Doncho, **kwargs):
    print(f'Doncho has {Doncho}. He is stupid!')

def congrats_maria(Maria, **kwargs):
    print(f'Maria has {Maria}. She is smart!')

numbers = [1, 2, 3, 4, 5]
grades_dict = {

    'Doncho': 3,
    'Ivan': 4,
    'Maria': 6,
    'Pesho': 4.5

}

shame_doncho(**grades_dict)   # Doncho has 3. He is stupid!
congrats_maria(**grades_dict) # Maria has 6. She is smart!

