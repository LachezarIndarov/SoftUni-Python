"""
input1
5
4
- X V -
- S - V
- - - -
X - - -
up
right
down
right
Christmas morning

output1
- - - -
- - - S
- - - -
X - - -
Good job, Santa! 2 happy nice kid/s.

Comments:
Santa has 5 presents. The size of the matrix is 4. After we receive the matrix, we start reading commands.
The first one is "up". The "X" means there is a naughty kid, so Santa moves on without dropping any presents.
Next, he reaches a nice kid and drops a present. The "down" command moves Santa to an empty cell.
The last command before the "Christmas morning" message is "right". Again we have a nice kid.
The count of nice kids reached 2, and we don't have any nice kids without presents left. So we print the appropriate message.

input2
3
4
- - - -
V - X -
- V C V
- - - S
left
up

output2
Santa ran out of presents!
- - - -
V - - -
- - S -
- - - -
No presents for 1 nice kid/s.

Comments:
The commands send Santa to a cell with a cookie, so all of the kids around him receive presents.
He runs out of presents because we have 3 kids there and only 3 presents.
The program ends, and we have 1 nice kid that hasn't received a present.

"""
def get_next_pos(row, col, direction):
    if direction == 'up':
        return row - 1, col
    if direction == 'down':
        return row + 1, col
    if direction == 'left':
        return row, col - 1
    if direction == 'right':
        return row, col + 1

def is_inside(row, col, size):
   return 0 <= row < size and 0 <= col < size


def get_around_kids(matrix, row, col):
    result = []
    if is_inside(row, col - 1, len(matrix)) and matrix[row][col - 1] == 'X' or matrix[row][col - 1] == 'V':
        result.append([row, col - 1])
    if is_inside(row, col + 1, len(matrix)) and matrix[row][col + 1] == 'X' or matrix[row][col + 1] == 'V':
        result.append([row, col + 1])
    if is_inside(row - 1, col, len(matrix)) and matrix[row - 1][col] == 'X' or matrix[row - 1][col] == 'V':
        result.append([row - 1, col])
    if is_inside(row + 1, col, len(matrix)) and matrix[row + 1][col] == 'X' or matrix[row + 1][col] == 'V':
        result.append([row + 1, col])

    return result


gifts = int(input())
size = int(input())

santa_row = 0
santa_col = 0
nice_kids = 0

matrix = []

for row in range(size):
    row_elements = input().split()
    for col in range(size):
        if row_elements[col] == 'S':
            santa_row = row
            santa_col = col
        elif row_elements[col] == 'V':
            nice_kids += 1
    matrix.append(row_elements)

nice_kids_gifted = 0

while gifts > 0:
    line = input()
    if line =='Christmas morning':
        break

    matrix[santa_row][santa_col] = '-'
    santa_row, santa_col = get_next_pos(santa_row, santa_col, line)

    if matrix[santa_row][santa_col] == 'V':
        gifts -= 1
        nice_kids_gifted += 1
    elif matrix[santa_row][santa_col] == 'C':
        around_kids = get_around_kids(matrix, santa_row, santa_col)
        for kid_row, kid_col in around_kids:
            if matrix[kid_row][kid_col] == 'V':
                nice_kids_gifted += 1
            gifts -= 1
            matrix[kid_row][kid_col] = '-'
            if gifts == 0:
                break

    matrix[santa_row][santa_col] = 'S'

if nice_kids_gifted != nice_kids and gifts == 0:
    print(f'Santa ran out of presents!')

for row in matrix:
    print(*row, sep=' ')


if nice_kids_gifted == nice_kids:
    print(f"Good job, Santa! {nice_kids} happy nice kid/s.")
else:
    print(f"No presents for {nice_kids - nice_kids_gifted} nice kid/s.")