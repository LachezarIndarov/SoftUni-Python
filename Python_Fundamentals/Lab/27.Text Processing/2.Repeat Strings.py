"""
Input1
hi abc add

Output1
hihiabcabcabcaddaddadd

Input2
work

Output2
workworkworkwork

Input3
ball

Output3
ballballballball

"""

words = input().split()
output = ""

for word in words:


    output += word * len(word)

print(output)