n = 15


print(list(range(n))) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
print(tuple(range(n))) # (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14)

#------------------------------------------------------------------------------

#         0  1  2  3  4  5  6  7  8  9 10 11  12 13 14 15
tuples = (1, 2, 3, 2, 4, 5, 1, 2, 3, 4, 5, 3, 3, 6, 7, 8, 1)

tuples2 = ('1', '2','3','2','4','5','1','2','3','4','5','3','3','6','7','8')
"""
1 -> 2
2 -> 2
3 -> 4
"""

print(tuples)
print('---count method---')
print(tuples.count(1))  # 2
print(tuples.count(2))  # 3
print(tuples.count(3))  # 4

#---------------------------------------------------------------------------
print('---index method----')
print(tuples.index(1))     # 0    Намерими първата единица в tuples        # equivalent to tuple.index(1,0)
print(tuples.index(1, 1))  # 6    Намерими първата единица след индекс 1   # equivalent to tuple.index(1,1)
print(tuples.index(1, 7))  # Nothing   Намерими първата единица след индекс 7   # equivalent to tuple.index(1,7)

print('---in----') # Проверяваме дадена стойност дали я има в tuples
print( 1 in tuples) # Проверяваме 1 дали я има в tuple
print(17 in tuples) # Проверяваме 17 дали я има в tuple

print('---loops---')
for value in tuples:
    print(value)

print('--- list comprehensions ---')
[print(x) for x in tuples]

print('---- other objects ---')
print(f'str.join(): {", ".join(tuples2)}')  # str.join(): 1, 2, 3, 2, 4, 5, 1, 2, 3, 4, 5, 3, 3, 6, 7, 8
print(f'len(): {len(tuples)}')              # len(): 17

print('---- tuple concatenation ----')
print((1,2) + (3,4,5)) # (1, 2, 3, 4, 5)

