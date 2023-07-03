values = [1, -1,  2, 1, 3, 4, 5, 6, 1, 2, 3, 4, -100]

print(values)                                       # [1, -1, 2, 1, 3, 4, 5, 6, 1, 2, 3, 4, -100]
print(sorted(values)) # new list, that is sorted    # [-100, -1, 1, 1, 1, 2, 2, 3, 3, 4, 4, 5, 6]
print(values)                                       # [1, -1, 2, 1, 3, 4, 5, 6, 1, 2, 3, 4, -100]

values.sort()         # sorts the list
print(values)                                       # [-100, -1, 1, 1, 1, 2, 2, 3, 3, 4, 4, 5, 6]


print(

    sorted(
        [1, -1, 2, 1, 4, -100]                  # [-100, -1, 1, 1, 2, 4]

    )
)

print(
    sorted(
        ['Pesho', 'Doncho', 'Gosho', 'Maria']   # ['Doncho', 'Gosho', 'Maria', 'Pesho']
    )
)

print(
    sorted(
        [(1, 7), (-1, 3), (1, 4)]               # [(-1, 3), (1, 4), (1, 7)]
    )
)


#-------------------------------------------------------------------------------------------

print(
    sorted(
        [1,5,-1, -5, -8, 2, 7, 4, -100],
        key=lambda  x: (x % 5, x)
    )
)       #  [-100, -5, 5, 1, -8, 2, 7, -1, 4]

#-------------------------------------------------------------------------------------------

def order_by_reminder_5(x):
    return (x % 5, x)

print(
    sorted(
        [1, 5, -1, -5, -8, 2, 7, 4, -100],
        key=order_by_reminder_5
    )

)     #  [-100, -5, 5, 1, -8, 2, 7, -1, 4]


dictionary1 = {

    'Peter': 21,
    'George': 18,
    'John': 45,

}

print(dictionary1)                             # {'Peter': 21, 'George': 18, 'John': 45}
print(dictionary1.items())                     # dict_items([('Peter', 21), ('George', 18), ('John', 45)])
sorted_dictionary = sorted(dictionary1.items())
print(sorted(dictionary1))                     # ['George', 'John', 'Peter']
print(sorted_dictionary) # sorting by name     # [('George', 18), ('John', 45), ('Peter', 21)]

print(
    sorted(
    dictionary1.items(),
    key=lambda x: x[1]
))                      # sorting by age       #  [('George', 18), ('Peter', 21), ('John', 45)]


print(
    sorted(
    dictionary1.items(),
    key=lambda x: x[1],
    reverse = True
))            # sorting by reversed age       #  [('John', 45), ('Peter', 21), ('George', 18)]