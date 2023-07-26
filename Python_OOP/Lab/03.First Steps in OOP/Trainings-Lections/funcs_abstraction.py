# enables extensibility
def print_list(list):
    print(list)

list1 = [1, 2, 3, 4, 5, 6]
print("Printing first list")
print_list(list1)
# Printing first list
# [1, 2, 3, 4, 5, 6]


list2 = [6, 5, 4, 3, 2, 1]
print("Printing second list")
print_list(list2)
# Printing second list
# [6, 5, 4, 3, 2, 1]

#---------------------------------------------------------------

def print_list(list):
    [print(x) for x in list]

list1 = [1, 2, 3, 4, 5, 6]
print("Printing first list")
print_list(list1)
# Printing first list
# 1
# 2
# 3
# 4
# 5
# 6


list2 = [6, 5, 4, 3, 2, 1]
print("Printing second list")
print_list(list2)
# Printing second list
# 6
# 5
# 4
# 3
# 2
# 1

#--------------------------------------------

def print_list(list):
    for x in list:
        if x is None:
            continue
        if x == 1:
            print('One')
        elif x == 2:
            print('Two')
        else:
            print(x)

list1 = [1, 2, 3, 4, 5, 6]
print("Printing first list")
print_list(list1)
# Printing first list
# One
# Two
# 3
# 4
# 5
# 6


list2 = [6, 5, 4, 3,None, 2, 1,None]
print("Printing second list")
print_list(list2)

# Printing second list
# 6
# 5
# 4
# 3
# Two
# One


#-------------------------------------------------
def get_name(number):
    if number == 1:
        return 'One'
    elif number == 2:
        return 'Two'
    else:
        return number

def print_list(list):
    for x in list:
        if x is None:
            continue
        print(get_name(x))

list1 = [1, 2, 3, 4, 5, 6]
print("Printing first list")
print_list(list1)

# Printing first list
# One
# Two
# 3
# 4
# 5
# 6

list2 = [6, 5, 4, 3, None, 2, 1,None]
print("Printing second list")
print_list(list2)

# Printing second list
# 6
# 5
# 4
# 3
# Two
# One

