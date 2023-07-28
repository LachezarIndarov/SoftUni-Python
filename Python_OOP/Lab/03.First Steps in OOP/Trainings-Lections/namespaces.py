def sum(list):
    result = 1
    for x in list:
        result += x
    return result
print(sum([1, 2, 3, 4])) # 11

#---------------------------------

# Global namespace - pi and sum1 (global for this module)
from math import pi

def sum1(list):
    # result and x - in local namespace(local for func and class)
    result = 1
    for x in list:
        result += x
    return result

print(sum1([1, 2, 3, 4])) # 11
print(pi) # 3.141592653589793


#------------------------------------------
# Global namespace - pi and sum1 (global for this module)
from math import pi

def f1():
    pi = 3.14
    print(pi)

def sum1(list):
    # result and x - in local namespace(local for func and class)
    result = 1
    for x in  list:
        result += x
    return result

#print and sum - built-in namespace
print(sum([1, 2, 3, 4]))
print(sum1([1, 2, 3, 4]))