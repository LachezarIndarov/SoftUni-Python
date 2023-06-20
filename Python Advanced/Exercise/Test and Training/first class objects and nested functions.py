list = [1, 2, 3]

print(1 in list)   # True
print(len(list))   # 3
print(list.pop())  # 3
print(list[0])     # 1

#-------------------------------------------
# nested functions
def f1():
    def f2():
        print('I am f2' )

    print('I am f1')
    f2()
f1()


#--------------------------------------------

def f1():
    def f2():
        def f3():
            print('I am f3')

        print('I am f2')
        f3()

    print('I am f1')
    f2()

f1()

#-----------------------------------------------


def math_operation(operation,*args):
    def add(*args):
        return sum(args)

    def substract(*args):
        return sum(-x for x in args)

    def multiply(*args):
        result = 1
        for x in args:
            result *= x
        return result
    if operation == '+':
        return add(*args)
    elif operation == '-':
        return substract(*args)
    elif operation == '*':
        return multiply(*args)
    else:
        return None

print(math_operation('+', 1, 2, 3, 4)) # 1 + 2 + 3 + 4 = 10
print(math_operation('-', 1, 2, 3, 4)) # -1 + -2 + -3 + -4 = -10
print(math_operation('*', 1, 2, 3, 4)) # 1 * 2 * 3 * 4 = 24

#-------------------------------------------------------------

def math_operation_factory(operation):
    def add(*args):
        return sum(args)

    def substract(*args):
        return sum(-x for x in args)

    def multiply(*args):
        result = 1
        for x in args:
            result *= x
        return result
    if operation == '+':
        return add
    elif operation == '-':
        return substract
    elif operation == '*':
        return multiply
    else:
        return None

add = math_operation_factory('+')
print(add(1, 2, 3))     # 6
print(add(1, -2, 4))    # 3

subtract = math_operation_factory('-')
print(subtract(1, 2, 3))  # -6
print(subtract(1, -2, 4)) # -3

add1 = math_operation_factory('+')
add2 = math_operation_factory('+')
print(add1 == add2)      # False

#-----------------------------------------------------

def order_by_factory(type):

    def by_value(x):
        return x

    def by_len(x):
        return len(x)

    if type == 'len':
        return  by_len
    else:
        return  by_value

print(
    sorted(
        [1, -2, 3, -4, 5, -7],
        key=order_by_factory('value')
    ),

)     #  [-7, -4, -2, 1, 3, 5]

print(
    sorted(
        ['Doncho', 'Pesho', 'Gosho'],
        key=order_by_factory('value')
    ),

)    # ['Doncho', 'Gosho', 'Pesho']

print(
    sorted(
        ['Alexandar', 'Doncho', 'Pesho', 'Gosho' ],
        key=order_by_factory('len')
    ),

)    # ['Pesho', 'Gosho', 'Doncho', 'Alexandar']


