#single-dimension list
list = [1, 2, 3, 4, 5, 6]
print(list) # [1, 2, 3, 4, 5, 6]

list.append(-11)
print(list) # [1, 2, 3, 4, 5, 6, -11]

list.pop()
print(list) # [1, 2, 3, 4, 5, 6]


#two-dimension list - list of lists
mm = [
    [1, 2, 3],
    [2, 3, 4],
    [3, 4, 5],
    [4, 5, 6]
]
print(mm) # [[1, 2, 3], [2, 3, 4], [3, 4, 5], [4, 5, 6]]

mm.append([-11])
print(mm) # [[1, 2, 3], [2, 3, 4], [3, 4, 5], [4, 5, 6], [-11]]

mm.pop()
print(mm) # [[1, 2, 3], [2, 3, 4], [3, 4, 5], [4, 5, 6]]

print(list[1]) # 2
print(mm[1])   # [2, 3, 4]

# three - dimensional list  - list of lists of lists

cc = [

    [ # 0
        [1, 2, 3],
        [2, 3, 4],
        [3, 4, 5],
    ],
    [ # 1

        [4, 5, 6],
        [5, 6, 7],
        [6, 7, 8],

    ],
    [ # 2

        [7, 8, 9],
        [8, 9, 10],
        [9, 10, 11],

    ],


]