"""
input1
Ali, Marry, Kim, Teddy, Monika, John

output1
["Monika", "Marry", "Teddy", "John", "Ali", "Kim"]

input2
Lilly, Tim, Kate, Tom, Alex

output2
['Lilly', 'Alex', 'Kate', 'Tim', 'Tom']

"""

names = input().split(", ")

sorted_names = sorted(names)
sorted_names = sorted(sorted_names, key=lambda name: -len(name))

print(sorted_names)
