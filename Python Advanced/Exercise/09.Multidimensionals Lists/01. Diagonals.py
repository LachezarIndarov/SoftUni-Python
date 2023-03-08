"""
input1
3
1, 2, 3
4, 5, 6
7, 8, 9


output1
Primary diagonal: 1, 5, 9. Sum: 15
Secondary diagonal: 3, 5, 7. Sum: 15

"""

size = int(input())

matrix = []
for i in range(size):
    matrix.append([int(x) for x in input().split(', ')])


primary = []
secondary = []

for index in range(size):
    primary.append(matrix[index][index])
    secondary.append(matrix[index][size - 1 - index])

print(f'Primary diagonal: {", ".join([str(x) for x in primary])}. Sum: {sum(primary)}')
print(f'Secondary diagonal: {", ".join([str(x) for x in secondary])}. Sum: {sum(secondary)}')