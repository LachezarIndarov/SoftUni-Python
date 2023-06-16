matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]

[print(row) for row in matrix]
"""
before change

[1, 2, 3]
[4, 5, 6]
[7, 8, 9]
"""
matrix[1][2] = 7
[print(row) for row in matrix]

"""
after change 7

[1, 2, 3]
[4, 5, 7]
[7, 8, 9]

"""