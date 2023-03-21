"""
input1
5 6
.....P
......
...B..
......
......
ULDDDR

output1
......
...B..
..BBB.
...B..
......
won: 0 5

input2
4 5
.....
.....
.B...
...P.
LLLLLLLL

output2
.B...
BBB..
BBBB.
BBB..
dead: 3 1

input3
5 8
.......B
...B....
....B..B
........
..P.....
ULLL

output3
BBBBBBBB
BBBBBBBB
BBBBBBBB
.BBBBBBB
..BBBBBB
won: 3 0

"""

"""
#!!!!!Variant 1 don't work correct 
def get_next_pos(row, col, command):
    if command == 'U':
        return row - 1, col
    if command == 'D':
        return row + 1, col
    if command == 'L':
        return row, col - 1
    if command == 'R':
        return row, col + 1

def is_outside(row, col, rows,cols):
    return row < 0 or col < 0 or row >= rows or col >= cols


def get_children(row,col,rows,cols):
    possible_children = [

        [row - 1, col],
        [row, col - 1],
        [row, col + 1],
        [row + 1, col]

    ]

    result = []
    for child_row, child_col in possible_children:
        if not is_outside(child_row, child_col, rows ,cols):
            result.append([child_row,child_col])
    return result

rows, cols = [int(x) for x in input().split()]

bunnies = set()
player_row = 0
player_col = 0

matrix = []

for row in range(rows):
    #.....P
    row_elements = list(input())
    for col in range(cols):
        if row_elements == 'P':
            player_row = row
            player_col = col
        elif row_elements[col] == 'B':
            bunnies.add(f'{row} {col}')
    matrix.append(row_elements)

commands = input()

won = False
dead = False


for command in commands:
    next_row, next_col = get_next_pos(player_row, player_col, command)
    matrix[player_row][player_col] = '.'

    if is_outside(next_row, next_col, rows, cols):
        won = True
    elif matrix[next_row][next_col] == 'B':
        dead = True
    else:
        matrix[next_row][next_col] = 'P'
        player_row, player_col = next_row, next_col

    new_bunnies = set()
    for bunny in bunnies:
        bunny_row, bunny_col = [int(x) for x in bunny.split()]
        children = get_children(bunny_row, bunny_col, rows, cols)
        for child_row, child_col in children:
            new_bunnies.add(f'{child_row} {child_col}')
            matrix[child_row][child_col] = 'B'
            if child_row == player_row and child_col == player_col:
                dead = True

    bunnies = bunnies.union(new_bunnies)
#    print()
    if won or dead:
        break

for row in matrix:
    print(''.join(row))

if won:
    print(f'won: {player_row} {player_col}')
else:
    print(f'dead: {player_row} {player_col}')
    
"""



#Variant2 work 100 in Judge

rows, cols = [int(item) for item in input().split()]
matrix = []

for _ in range(rows):
    matrix.append(list(input()))

commands = input()

# End of inputs


def find_player(matrix):
    stop = False
    postion = ()
    for r in range(rows):
        if stop:
            break
        for c in range(cols):
            if matrix[r][c] == 'P':
                postion = (r, c)
                stop = True
    return postion


def multiply_bunny(matrix, dead):
    bunnies_location = []
    for r in range(len(matrix)):
        for c in range(len(matrix[r])):
            if matrix[r][c] == 'B':
                bunnies_location.append((r, c))

    for bun in bunnies_location:
        up = (bun[0] - 1, bun[1])
        down = (bun[0] + 1, bun[1])
        left = (bun[0], bun[1] - 1)
        right = (bun[0], bun[1] + 1)

        if 0 <= up[0] < rows and 0 <= up[1] < cols:
            if matrix[up[0]][up[1]] == 'P':
                dead = True
            matrix[up[0]][up[1]] = 'B'
        if 0 <= down[0] < rows and 0 <= down[1] < cols:
            if matrix[down[0]][down[1]] == 'P':
                dead = True
            matrix[down[0]][down[1]] = 'B'
        if 0 <= left[0] < rows and 0 <= left[1] < cols:
            if matrix[left[0]][left[1]] == 'P':
                dead = True
            matrix[left[0]][left[1]] = 'B'
        if 0 <= right[0] < rows and 0 <= right[1] < cols:
            if matrix[right[0]][right[1]] == 'P':
                dead = True
            matrix[right[0]][right[1]] = 'B'

    return dead, matrix


def move_player(loc, go, matrix, dead):
    out = False
    last = loc
    if go == 'U':
        new = (loc[0] - 1, loc[1])
        if 0 <= new[0] < rows and 0 <= new[1] < cols:
            last = new
            if matrix[new[0]][new[1]] == 'B':
                dead = True
                return last, dead, out, matrix
            else:
                matrix[new[0]][new[1]] = 'P'
                matrix[loc[0]][loc[1]] = '.'
                return last, dead, out, matrix
        else:
            out = True
            matrix[last[0]][last[1]] = '.'
            return last, dead, out, matrix

    elif go == 'D':
        new = (loc[0] + 1, loc[1])
        if 0 <= new[0] < rows and 0 <= new[1] < cols:
            last = new
            if matrix[new[0]][new[1]] == 'B':
                dead = True
                return last, dead, out, matrix
            else:
                matrix[new[0]][new[1]] = 'P'
                matrix[loc[0]][loc[1]] = '.'
                return last, dead, out, matrix
        else:
            out = True
            matrix[last[0]][last[1]] = '.'
            return last, dead, out, matrix

    elif go == 'L':
        new = (loc[0], loc[1] - 1)
        if 0 <= new[0] < rows and 0 <= new[1] < cols:
            last = new
            if matrix[new[0]][new[1]] == 'B':
                dead = True
                return last, dead, out, matrix
            else:
                matrix[new[0]][new[1]] = 'P'
                matrix[loc[0]][loc[1]] = '.'
                return last, dead, out, matrix
        else:
            out = True
            matrix[last[0]][last[1]] = '.'
            return last, dead, out, matrix

    elif go == 'R':
        new = (loc[0], loc[1] + 1)
        if 0 <= new[0] < rows and 0 <= new[1] < cols:
            last = new
            if matrix[new[0]][new[1]] == 'B':
                dead = True
                return last, dead, out, matrix
            else:
                matrix[new[0]][new[1]] = 'P'
                matrix[loc[0]][loc[1]] = '.'
                return last, dead, out, matrix
        else:
            out = True
            matrix[last[0]][last[1]] = '.'
            return last, dead, out, matrix

    return last, dead, out, matrix

# Main 
dead = False
where = find_player(matrix)
for ch in commands:
    where, dead, out, matrix = move_player(where, ch, matrix, dead)
    dead, matrix = multiply_bunny(matrix, dead)
    if dead or out:
        break

if dead:
    for row in matrix:
        print(*row, sep="")

    print("dead: ", end='')
    print(*where, sep=' ')
else:
    for row in matrix:
        print(*row, sep="")
    print("won: ", end='')
    print(*where, sep=' ')
