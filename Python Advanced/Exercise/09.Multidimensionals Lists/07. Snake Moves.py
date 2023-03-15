"""
input1
5 6
SoftUni

output1
SoftUn
UtfoSi
niSoft
foSinU
tUniSo


input2
1 4
Python

output2
Pyth

"""

rows, cols  = [int(x) for x in input().split()]
word = input()

index = 0

for row in range(rows):
    elements = [None] * cols
    start, end, step = (0, cols, 1) if row % 2 == 0 else (cols - 1, - 1, -1)
    for col in range(start, end, step):
        elements[col] = word[index % len(word)]
        index += 1
    print(''.join(elements))