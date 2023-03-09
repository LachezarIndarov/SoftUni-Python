"""
input1
3
11 2 4
4 5 6
10 8 -12

output1
15

Comments:
Primary diagonal: sum = 11 + 5 + (-12) = 4
Secondary diagonal: sum = 4 + 5 + 10 = 19
Difference: |4 - 19| = 15

input2
4
-7 14 9 -20
3 4 9 21

output2
34

"""

size = int(input())

matrix = []
for i in range(size):
    matrix.append([int(x) for x in input().split()])


primary = []
secondary = []

for index in range(size):
    primary.append(matrix[index][index])
    secondary.append(matrix[index][size - 1 - index])

primary_sum = sum(primary)
secondary_sum = sum(secondary)

print(abs(primary_sum - secondary_sum))