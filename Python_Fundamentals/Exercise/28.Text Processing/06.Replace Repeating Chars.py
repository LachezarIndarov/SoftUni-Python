"""
Input1                                  Output1
aaaaabbbbbcdddeeeedssaa                 abcdedsa

Input2                                  Output2
qqqwerqwecccwd                          qwerqwecwd
"""
# Variant 1
text = input()
print("".join([text[i] for i in range(len(text)) if text[i] != text[i - 1] or i == 0]))


"""
Variant 2

o_string = input()
opt_string = o_string[0]

for idx in range(1, len(o_string)):
    if o_string[idx-1] != o_string[idx]:
        opt_string += o_string[idx]
print(opt_string)

"""

"""
Variant 3

text = input()
optimisiran_string = text[0]



for i in range(1, len(text)):
    text1 = text[i - 1] 
    text2 = text[i]     
    if text[i-1] != text[i]:
        optimisiran_string += text[i]
print(optimisiran_string)


"""