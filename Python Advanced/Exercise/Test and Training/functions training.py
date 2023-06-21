def f(name,town, age):
    return (f'This is {name} from {town} and he is {age} years old')

info1 = {

    'name': 'Pesho',
    'town': 'Burgas',
    'age': 48,

}

info2 = {

    'name': 'Lacho',
    'town': 'Smolyan',
    'age': 22,

}

print(info1)  # {'name': 'Pesho', 'town': 'Burgas', 'age': 48}
print(info2)  # {'name': 'Lacho', 'town': 'Smolyan', 'age': 22}


print(f(**info1)) # This is Pesho from Burgas and he is 48 years old
print(f(**info2)) # This is Lacho from Smolyan and he is 22 years old