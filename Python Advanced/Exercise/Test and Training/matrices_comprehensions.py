list = [1, 2, 3, 4, 5]

list2 = []

for i in list:
    list2.append(i + 1)

print(list)  # [1, 2, 3, 4, 5]
print(list2) # [2, 3, 4, 5, 6]

list3 = [i + 1 for i in list]
print(list3) # [2, 3, 4, 5, 6] - list comprehensions

mm = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [10, 11, 12]

]


print(mm) # [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]

print([i + 1 for row in mm for i in row]) #[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13] - list comprehensions

# comprehensions in comprehensions - nested comprehensions
print([[i + 1 for i in row] for row in mm]) # [[2, 3, 4], [5, 6, 7], [8, 9, 10], [11, 12, 13]] - matrices comprehensions


print(

    # Multi Dimension comprehensions
    # Flattering comprehensions
    [
        i + 1
        for row in mm
            for i in row

    ]
) # [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]