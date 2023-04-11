"""
Test Code1
dictionary = {'name': 'Peter', 'age': 25}

print(kwargs_length(**dictionary))

output1
2

Test Code2
dictionary = {}

print(kwargs_length(**dictionary))

output2
0

"""

def kwargs_length(**kwargs):
    return len(kwargs)

dictionary = {'name': 'Peter', 'age': 25, 'gender': 'male'}

print(kwargs_length(**dictionary))
# print(kwargs_length(name='Peter', age = 25))
