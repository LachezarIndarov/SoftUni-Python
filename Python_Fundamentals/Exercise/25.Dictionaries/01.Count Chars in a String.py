"""
input1
text

output1
t -> 2
e -> 1
x -> 1

Input2
text text text

output2
t -> 6
e -> 3
x -> 3

"""
from collections import Counter

word = input()
result = Counter(word)

for key, value  in result.items():
    if key != " ":
        print(f"{key} -> {value}")






