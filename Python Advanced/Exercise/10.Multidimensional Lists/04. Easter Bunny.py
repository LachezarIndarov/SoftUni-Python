"""
input1
5
1 3 7 9 11
X 5 4 X 63
7 3 21 95 1
B 1 73 4 9
9 2 33 2 0

output1
right
[3, 1]
[3, 2]
[3, 3]
[3, 4]
87

Comments:
The number of eggs if the bunny goes up is equal to 7. If he goes down = 9, there are no eggs on the left and 87 on the right.
That's why the bunny should follow this direction (right) and collect the eggs provided there.

input2
8
4 18 9 7 24 41 52 11
54 21 19 X 6 34 75 57
76 67 7 44 76 27 56 37
92 35 25 37 52 34 56 72
35 X 1 45 4 X 37 63
105 X B 2 12 43 5 19
48 19 35 20 32 27 42 4
73 88 78 32 37 52 X 22


output2
down
[6, 2]
[7, 2]
113

"""
size = int(input())
matrix = []

bunny_row = 0
bunny_col = 0

for row in range(size):
    row_elements = input().split()
    for col in range(size):
        if row_elements[col] == 'B':
            bunny_row = row
            bunny_col = col
    matrix.append(row_elements)

directions = {

    'right': lambda r, c: (r, c + 1),
    'left' : lambda r, c: (r, c - 1),
    'up'   : lambda r, c: (r - 1, c),
    'down' : lambda r, c: (r + 1, c),

}
best_sum = float('-inf')
best_dir = ''
best_path = []

for direction in directions:
    current_sum = 0
    row, col = directions[direction](bunny_row, bunny_col)
    current_path = []

    while 0 <= row < size and 0 <= col < size and matrix[row][col] != 'X':
        current_sum += int(matrix[row][col])
        current_path.append([row, col])
        row, col = directions[direction](row, col)

    if current_sum > best_sum:
        best_sum = current_sum
        best_dir = direction
        best_path = current_path

print(best_dir)
print(*best_path, sep='\n')
print(best_sum)


