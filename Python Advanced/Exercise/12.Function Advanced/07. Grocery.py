"""
Test Code1
print(grocery_store(
    bread=5,
    pasta=12,
    eggs=12,
))

output1
pasta: 12
eggs: 12
bread: 5

Test Code2
print(grocery_store(
    bread=2,
    pasta=2,
    eggs=20,
    carrot=1,
))

output2
eggs: 20
bread: 2
pasta: 2
carrot: 1

"""

def grocery_store(**kwargs):
    sorted_result = [f'{key}: {value}' for key, value in sorted(kwargs.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))]
    return  '\n'.join(sorted_result)

print(grocery_store(
    bread=2,
    pasta=2,
    eggs=20,
    carrot=1,
))

