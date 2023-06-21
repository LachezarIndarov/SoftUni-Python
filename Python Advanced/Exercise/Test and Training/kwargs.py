def f(**kwargs): # key-value args
    print(kwargs)

print(f(name='Lachezar', age=22))        # {'name': 'Lachezar', 'age': 22}
print(f(x=1, y=-11))                     # {'x': 1, 'y': -11}
print(f(values = [1,2,3,4], pair=(7,6))) # {'values': [1, 2, 3, 4], 'pair': (7, 6)}

#----------------------------------------------

def f2(**kwargs): # key-value args
    if 'age' not in kwargs:
        kwargs['age'] = None
    print(kwargs)

print(f2(name='Doncho', age=19))        # {'name': 'Doncho', 'age': 19}
print(f2(x=1, y=-11))                     # {'x': 1, 'y': -11, 'age': None}
print(f2(values = [1,2,3,4], pair=(7,6))) # {'values': [1, 2, 3, 4], 'pair': (7, 6), 'age': None}

#------------------------------------------------