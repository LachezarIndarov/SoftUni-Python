"""
input1
1, 2, 3, 4, 5
2

output1
[9, 6]

input2
3, 4, 5, 1, 29, 4
6

output2
[3, 4, 5, 1, 29, 4]

input3
100, 94, 24, 99
5

output3
[100, 94, 24, 99, 0]

"""
numbers_strings = input().split(", ")
beggar = int(input())

beggar_count = []
element = 0

for i in range(beggar):
    beggar_count.append(0)

while element < len(numbers_strings):

    for k in range(len(beggar_count)):
        if element >= len(numbers_strings):
            break
        beggar_count[k] += int(numbers_strings[element])
        element += 1

print(beggar_count)

