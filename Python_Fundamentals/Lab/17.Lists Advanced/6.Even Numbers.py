"""
input1
3, 2, 1, 5, 8

output1
[1, 4]

input2
2, 4, 6, 9, 10

output2
[0, 1, 2, 4]

"""

strings = input().split(", ")
numbers = list(map(int, strings))

even_index_numbers = list()

for i in range(len(numbers)):
    if numbers[i] % 2 == 0:
        even_index_numbers.append(i)

print(even_index_numbers)

