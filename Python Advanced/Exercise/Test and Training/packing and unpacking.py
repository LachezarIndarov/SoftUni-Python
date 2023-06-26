# 1.Unpacking
list = [1, 2, 3, 4]

x = list[0]
y = list[1]
z = list[2]
a = list[3]

print(x) # 1
print(y) # 2
print(z) # 3
print(a) # 4

#-------------------------------

k, l , *r = list

print(k) # 1
print(l) # 2
print(r) # [3, 4]

#-------------------------------
k, *l , r = list

print(k) # 1
print(l) # [2, 3]
print(r) # 4

#-------------------------------
k, *_, r = list

print(k) # 1
print(r) # 4



# 2.Packing

def f(args):
    print(args)
print('----f()-----')
f(1)                 # 1
f([1, 2, 3])         # [1, 2, 3]
f({'x': 1, 'y': 2})  # {'x': 1, 'y': 2}
f({1, 2, 3})         # {1, 2, 3}

#-----------------------------------------

def f2(*args):
    print(args)


print('----f2()-----')
f2(1)                 # 1
f2([1, 2, 3])         # [1, 2, 3]
f2({'x': 1, 'y': 2})  # {'x': 1, 'y': 2}
f2({1, 2, 3})         # {1, 2, 3}
f2(1, 2)              # (1, 2)    - this is  tuple thanks to (*args)
f2(1, 2, 3)           # (1, 2, 3) - this is  tuple thanks to (*args)

#--------------------------------------------
def multiply(*args):
    print(args)

print(multiply(1))                          # (1,)
print(multiply(1,2))                        # (1, 2)
print(multiply(1, 2, 3, 4, 5, 6, 7, 8, 9))  # (1, 2, 3, 4, 5, 6, 7, 8, 9)

#---------------------------------------------
def multiply2(*args):
    product = 1
    for i in args:
        product *= i
    return product

print(multiply2(1))                          # 1
print(multiply2(1, 2))                       # 2
print(multiply2(1, 2, 3, 4, 5, 6, 7, 8, 9))  # 362880 


