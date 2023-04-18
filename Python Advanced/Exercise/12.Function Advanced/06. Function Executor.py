"""
Test Code1
def sum_numbers(num1, num2):
    return num1 + num2

def multiply_numbers(num1, num2):
    return num1 * num2

print(func_executor(
    (sum_numbers, (1, 2)),
    (multiply_numbers, (2, 4))
))

output1
sum_numbers - 3
multiply_numbers - 8


Test Code2
def make_upper(*strings):
    result = tuple(s.upper() for s in strings)
    return result

def make_lower(*strings):
    result = tuple(s.lower() for s in strings)
    return result

print(func_executor(
    (make_upper, ("Python", "softUni")),
    (make_lower, ("PyThOn",)),
))

output2
make_upper - ('PYTHON', 'SOFTUNI')
make_lower - ('python', )


"""

def func_executor(*args):
    result = []

    for func_ref, func_params in args:
        func_result = func_ref(*func_params)
        result.append(f'{func_ref.__name__} - {func_result}')
    return '\n'.join(result)

def sum_numbers(num1,num2):
    return num1 + num2

def abs_value(num1):
    return abs(num1)

def multiply_numbers(num1,num2,num3):
    return num1 * num2 * num3

print(func_executor(
    (abs_value, (5,)),
    (sum_numbers, (1,2)),
    (multiply_numbers, (2, 4, 3)),
))



