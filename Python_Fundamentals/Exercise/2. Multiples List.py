"""
input1
2
5

output1
[2, 4, 6, 8, 10]

input2
1
10

output2
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

"""

factor = int(input())
count = int(input())

my_list = []

for num in range(1,count+1):
    my_list.append(num * factor)

print(my_list)
