"""
input1
4
Ce O
Mo O Ce
Ee
Mo

output1
Ce
Ee
Mo
O

input2
3
Ge Ch O Ne
Nb Mo Tc
O Ne

output2
Ch
Ge
Mo
Nb
Ne
O
Tc
"""

n = int(input())

result = set()

for i in range(n):
    current_set = set(input().split())
    result = result.union(current_set)

for el in result:
    print(el)
