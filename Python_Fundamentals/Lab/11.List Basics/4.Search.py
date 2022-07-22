"""
input1
3
SoftUni
I study at SoftUni
I walk to work
I learn Python at SoftUni

output1
["I study at SoftUni", "I walk to work", "I learn Python at SoftUni"]
["I study at SoftUni", "I learn Python at SoftUni"]

input2
4
tomatoes
I love tomatoes
I can eat tomatoes forever
I don't like apples
Yesterday I ate two tomatoes

output2
["I love tomatoes", "I can eat tomatoes forever", "I don't like apples", "Yesterday I ate two tomatoes"]
["I love tomatoes", "I can eat tomatoes forever", "Yesterday I ate two tomatoes"]
"""

number = int(input())
search_word = input()
strings = list()
filtered = list()


for i in range(number):
    current_string = input()
    strings.append(current_string)
    if search_word in current_string:
        filtered.append(current_string)



print(strings)
print(filtered)