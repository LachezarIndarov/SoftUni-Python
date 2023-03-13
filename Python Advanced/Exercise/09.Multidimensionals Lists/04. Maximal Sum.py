"""
input1
4 5
1 5 5 2 4
2 1 4 14 3
3 7 11 2 8
4 8 12 16 4

output1
Sum = 75
1 4 14
7 11 2
8 12 16


input2
5 6
1 0 4 3 1 1
1 3 1 3 0 4
6 4 1 2 5 6
2 2 1 5 4 1
3 3 3 6 0 5


output3
Sum = 34
2 5 6
5 4 1
6 0 5


"""

rows, cols = [int(x) for x in input().split()]

matrix = []

for i in range(rows):
    matrix.append([int(x) for x in input().split()])

best_sum = float('-inf')
start_row = 0
start_col = 0

for row in range(rows - 2):
    for col in range(cols - 2):
        current_sum = matrix[row][col] + matrix[row][col + 1] + matrix[row][col + 2] + \
                      matrix[row + 1][col] + matrix[row + 1][col + 1] + matrix[row + 1][col + 2] + \
                      matrix[row + 2][col] + matrix[row + 2][col + 1] + matrix[row + 2][col + 2]


        if current_sum > best_sum:
            best_sum = current_sum
            start_row = row
            start_col = col

print(f'Sum = {best_sum}')
print(f'{matrix[start_row][start_col]} {matrix[start_row][start_col + 1]} {matrix[start_row][start_col + 2]}')
print(f'{matrix[start_row + 1][start_col]} {matrix[start_row + 1][start_col + 1]} {matrix[start_row + 1][start_col + 2]}')
print(f'{matrix[start_row + 2][start_col]} {matrix[start_row + 2][start_col + 1]} {matrix[start_row + 2][start_col + 2]}')
