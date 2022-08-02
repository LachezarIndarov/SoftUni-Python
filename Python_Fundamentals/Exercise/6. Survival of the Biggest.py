"""
input1
10 9 8 7 6 5
3

output1
10, 9, 8

input2
1 10 2 9 3 8
2

output2
10, 9, 3, 8

"""

numbers = input().split(" ")
count_of_numbers_remove = int(input())


for j in range(count_of_numbers_remove):

   for i in range(0, len(numbers)):
       numbers[i] = int(numbers[i])

   min_element = min(numbers)
   numbers.remove(min_element)

print(*numbers, sep=", ")