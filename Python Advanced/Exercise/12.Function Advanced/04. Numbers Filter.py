"""
input1
print(even_odd_filter(
    odd=[1, 2, 3, 4, 10, 5],
    even=[3, 4, 5, 7, 10, 2, 5, 5, 2],
))

output1
{'even': [4, 10, 2, 2], 'odd': [1, 3, 5]}

input2
print(even_odd_filter(
    odd=[2, 2, 30, 44, 10, 5],
))

output2
{'odd': [5]}

"""
def even_odd_filter(**kwargs):
    result = {}

    for key, value in kwargs.items():
        parity = 0 if key == 'even' else 1
        filtered = [x for x in value if x % 2 == parity]
        result[key] = filtered

    return  dict(sorted(result.items(), key=lambda x: -len(x[1])))


print(even_odd_filter(
    odd=[1, 2, 3, 4, 10, 5, 11, 17],
    even=[3, 4, 5, 7, 10, 2, 5, 5, 2],

))

print(even_odd_filter(
    odd=[1, 2, 3, 4, 10, 5],


))

print(even_odd_filter(
    even=[3, 4, 5, 7, 10, 2, 5, 5, 2],


))