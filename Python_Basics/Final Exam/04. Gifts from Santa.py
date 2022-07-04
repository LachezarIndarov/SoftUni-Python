"""
input1
1
30
15

output1
30 24 18 12 6

input2
1
36
12

output2
36 30 24 18

"""

n = int(input())
m = int(input())
s = int(input())

for i in range(m, n-1, -1):
    if i % 2 == 0 and i % 3 == 0:
        if i == s:
            break
        else:
            print(i, end=' ')