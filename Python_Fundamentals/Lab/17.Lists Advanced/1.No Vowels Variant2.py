"""
input1
Python

output1
Pythn

input2
ILovePython

output2
LvPythn
"""


#!!! List Comprehensions
GlasniEng = ["a","o","u","e","i"]
text = input()

No_GlasniEng = [ch for ch in text if ch not in GlasniEng]

print("".join(No_GlasniEng))
