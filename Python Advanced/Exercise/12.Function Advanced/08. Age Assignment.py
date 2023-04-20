"""
Test Code1
print(age_assignment("Peter", "George", G=26, P=19))

output1
George is 26 years old.
Peter is 19 years old.

Test Code2
print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))

output2
Amy is 22 years old.
Bill is 61 years old.
Willy is 36 years old.

"""
def age_assignment(*args, **kwargs):
    result = {}

    for name in args:
        first_letter = name[0]
        age = kwargs[first_letter]
        result[name] = age

    sorted_result = [f'{key} is {value} years old.' for key ,value in sorted(result.items(), key=lambda x: x[0])]
    return '\n'.join(sorted_result)

print(age_assignment("Peter", "George", G=26, P=19))
print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))

