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

GlasniEng = ["a","o","u","e","i"]

No_GlasniEng = list()

text = input()

for ch in text:
    if ch not in GlasniEng:
        No_GlasniEng.append(ch)

print("".join(No_GlasniEng))
