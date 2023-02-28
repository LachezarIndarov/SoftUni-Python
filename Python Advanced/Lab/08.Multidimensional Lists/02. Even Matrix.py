"""
input1
2
1, 2, 3
4, 5, 6

output1
[[2], [4, 6]]

input2
4
10, 33, 24, 5, 1
67, 34, 11, 110, 3
4, 12, 33, 63, 21
557, 45, 23, 55, 67

output2
[[10, 24], [34, 110], [4, 12], []]
"""

n = int(input())

result = []

for i in range(n):
    row = [int(x) for x in input().split(', ')]
    result.append([x for x in row if x % 2 == 0])

print(result)

"""
Variant2 with matrix

n = int(input())
matrix = [[int(x) for x in input().split(', ')] for i in range(n)]
print([[x for x in row if x % 2 == 0] for row in matrix])

"""

