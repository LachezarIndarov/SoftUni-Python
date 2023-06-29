"""
Sets:
- search ,add, remove is very ,very,very fast
- contains only unique values
- unordered
- ordered (with tree)

diference between dictionary and sets
sets = {1,2,3,4,5}
dictionary = { '1': 1,
               '2': 2,
               '3': 3
"""

sets = {1,2,3,4,5}
print(sets) # {1, 2, 3, 4, 5}

# this is an empty dictionaries, not a set
dict = {}

# This is an empty set
sets1 = set()

# add
sets.add(8)
print(sets) # {1, 2, 3, 4, 5, 8}

# remove
sets.remove(4)
print(sets) # {1, 2, 3, 5, 8}

# check if value is in set
print(4 in sets) # False
print(5 in sets) # True