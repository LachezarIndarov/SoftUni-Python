"""
Test Code1
print(even_odd(1, 2, 3, 4, 5, 6, "even"))

output1
[2, 4, 6]

Test Code2
print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))

output2
[1, 3, 5, 7, 9]

"""

def even_odd(*args):
    filter_command = args[-1]
    parity = 0 if filter_command == 'even' else 1
    result = []

    for index in range(len(args) - 1):
        number = args[index]
        if number % 2 == parity:
            result.append(number)

    return result

print(even_odd(1, 2, 3, 4, 5, 6, "even"))
print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))