"""
input1
3
1 2 3
4 5 6
7 8 9
Add 0 0 5
Subtract 1 1 2
END

output1
6 2 3
4 3 6
7 8 9

input2
4
1 2 3 4
5 6 7 8
8 7 6 5
4 3 2 1
Add 4 4 100
Add 3 3 100
Subtract -1 -1 42
Subtract 0 0 42
END


output2
Invalid coordinates
Invalid coordinates
-41 2 3 4
5 6 7 8
8 7 6 5
4 3 2 101

"""

size = int(input())
matrix = []

for i in range(size):
    matrix.append([int(x) for x  in input().split()])


while True:
    line = input()
    if line == 'END':
        break

    parts = line.split()
    command = parts[0]
    row, col, value = [int(x) for x in parts[1:]]

    if row < 0 or col < 0 or row >= size or col >= size:
        print('Invalid coordinates')
        continue

    if command == 'Add':
        matrix[row][col] += value
    else:
        matrix[row][col] -= value

for row in matrix:
    print(*row, sep=' ')