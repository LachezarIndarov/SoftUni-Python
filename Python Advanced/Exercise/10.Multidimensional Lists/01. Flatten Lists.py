"""
input1
1 2 3 |4 5 6 |  7  88

output1
7 88 4 5 6 1 2 3

input2
7 | 4  5|1 0| 2 5 |3

output2
3 2 5 1 0 4 5 7

input3
1| 4 5 6 7  |  8 9

output3
8 9 4 5 6 7 1

"""

sublists = input().split('|')

result = []

for index in range(len(sublists) -1, -1, -1):
    current_elements = sublists[index].strip().split()
    result.extend(current_elements)

print(' '.join(result))