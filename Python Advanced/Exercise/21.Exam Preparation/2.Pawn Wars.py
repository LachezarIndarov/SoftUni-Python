"""
input1
- - - - - - b -
- - - - - - - -
- - - - - - - -
- - - - - - - -
- - - - - - - -
- w - - - - - -
- - - - - - - -
- - - - - - - -

output1
Game over! White pawn is promoted to a queen at b8.

input2
- - - - - - - -
- - - - - - - -
- - - - - - - -
- - - - - - - -
- - - - - - - -
b - - - - - - -
- w - - - - - -
- - - - - - - -

output2
Game over! White win, capture on a3.


Comments:
We start by pushing the white pawn to b4, next, we push the black pawn to g7:
- - - - - - - -
- - - - - - b -
- - - - - - - -
- - - - - - - -
- w - - - - - -
- - - - - - - -
- - - - - - - -
- - - - - - - -
Then white play b5, black play g6:
- - - - - - - -
- - - - - - - -
- - - - - - b -
- w - - - - - -
- - - - - - - -
- - - - - - - -
- - - - - - - -
- - - - - - - -
…
Capturing is not possible here, so after a few more moves, the white pawn is promoted to a queen on b8.
A white pawn always start first, so it must capture the black one on a3 in the first move:
- - - - - - - -
- - - - - - - -
- - - - - - - -
- - - - - - - -
- - - - - - - -
w - - - - - - -
- - - - - - - -
- - - - - - - -


"""
size = 8
matrix = []
white_row, white_col, black_row, black_col = 0, 0, 0, 0
 
for r in range(8):
    line = input().split()
    for c in range(8):
        if line[c] == 'w':
            white_row = r
            white_col = c
        elif line[c] == 'b':
            black_row = r
            black_col = c
    matrix.append(line)
 
while True:
    if 0 <= white_row-1 < size and 0 <= white_col-1 < size and matrix[white_row-1][white_col-1] == 'b':
        print(f"Game over! White win, capture on {chr(97+black_col)}{8-black_row}.")
        break
    elif 0 <= white_row-1 < size and 0 <= white_col+1 < size and matrix[white_row-1][white_col+1] == 'b':
        print(f"Game over! White win, capture on {chr(97+black_col)}{8-black_row}.")
        break
    else:
        white_row -= 1
        matrix[white_row][white_col] = 'w'
        matrix[white_row-1][white_col] = '-'
        if white_row == 0:
            print(f'Game over! White pawn is promoted to a queen at {chr(97+white_col)}8.')
            break
    if 0 <= black_row+1 < size and 0 <= black_col-1 < size and matrix[black_row+1][black_col-1] == 'w':
        print(f"Game over! Black win, capture on {chr(97 + white_col)}{8-white_row}.")
        break
    elif 0 <= black_row+1 < size and 0 <= black_col+1 < size and matrix[black_row+1][black_col+1] == 'w':
        print(f"Game over! Black win, capture on {chr(97+white_col)}{8-white_row}.")
        break
    else:
        black_row += 1
        matrix[black_row][black_col] = 'b'
        matrix[black_row-1][black_col] = '-'
        if black_row == 7:
            print(f'Game over! Black pawn is promoted to a queen at {chr(97+black_col)}1.')
            break
