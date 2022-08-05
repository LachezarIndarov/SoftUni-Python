"""
input1
abc
3

output1
abcabcabc

input2
String
2

output2
StringString

"""

repeater = lambda str,count: str * count

current_string = input()
current_count = int(input())

print(repeater(current_string,current_count))