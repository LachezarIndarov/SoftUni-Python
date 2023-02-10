"""
input1
4 3
1
3
5
7
3
4
5

output1
3
5

input2
2 2
1
3
1
5

output2
1

"""
# intersection - check for the same elements in both 2 sets

n,m = [int(x) for x in input().split()]

first = set()
second = set()

for i in range(n):
    first.add(int(input()))

for i in range(m):
    second.add(int(input()))

result = first.intersection(second)
for num in result:
    print(num)