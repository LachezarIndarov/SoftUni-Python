"""
input1
3 4
A B B D
E B B B
I J B B

output2
2

Comments:
Two 2x2 squares of equal cells:
A B B D	A B B D
E B B B	E B B B
I J B B	I J B B


input2
2 2
a b
c d

output2
0

Comments:
No 2x2 squares of equal cells exist.

input3
5 4
A A B D
A A B B
I J B B
C C C G
C C K P

output3
3

Comments:
Three 2x2 squares of equal cells:
A A B D  A A B D  A A B D
A A B B  A A B B  A A B B
I J B B  I J B B  I J B B
C C C G  C C C G  C C C G
C C K P  C C K P  C C K P


"""

rows, cols = [int(x) for x in input().split()]

matrix = []

for i in range(rows):
    matrix.append(input().split())

squares = 0

for row in range(rows - 1):
    for col in range(cols - 1):
        if matrix[row][col] == matrix[row][col + 1] == matrix[row + 1][col] == matrix[row + 1][col + 1]:
            squares += 1

print(squares)

