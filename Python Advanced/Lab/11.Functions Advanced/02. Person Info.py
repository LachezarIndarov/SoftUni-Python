"""
input1
print(get_info(**{"name": "George", "town": "Sofia", "age": 20}))

output2
This is George from Sofia and he is 20 years old
"""
def get_info(name,town, age):
    return (f'This is {name} from {town} and he is {age} years old')