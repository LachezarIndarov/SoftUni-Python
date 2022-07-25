"""
input1
5
33
19
-2
18
998
even

output1
[-2, 18, 998]

input2
3
111
-4
0
negative

output2
[-4]

"""

number = int(input())

numbers_list = list()

for i in range(number):
    current = int(input())
    numbers_list.append(current)

filter_word = input()
filtered = list()

for current_number in numbers_list:
    if filter_word == "even" and current_number % 2 == 0:
            filtered.append(current_number)
    if filter_word == "odd" and current_number % 2 != 0:
            filtered.append(current_number)
    if filter_word == "positive":
        if current_number >= 0:
            filtered.append(current_number)
    if filter_word == "negative":
        if current_number < 0:
            filtered.append(current_number)

print(filtered)




