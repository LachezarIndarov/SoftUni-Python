# print even numbers from matrix
matrix = [

    [1,2,3,4],
    [2,3,4,5],
    [3,4,5,6],

]

def remove_even(list):
    return [x for x in list if x % 2 == 0]

print([remove_even(row) for row in matrix]) # [[2, 4], [2, 4], [4, 6]]