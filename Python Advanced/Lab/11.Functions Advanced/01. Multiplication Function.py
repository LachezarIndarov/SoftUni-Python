"""
input1
print(multiply(1, 4, 5))
print(multiply(4, 5, 6, 1, 3))
print(multiply(2, 0, 1000, 5000))

output1
20
360
0


"""
def multiply(*args):
    product = 1

    for i in args:
        product *= i

    return product

