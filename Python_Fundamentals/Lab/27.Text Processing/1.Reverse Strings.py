"""
input1

helLo
Softuni
bottle
end

Output1

helLo = oLleh
Softuni = inutfoS
bottle = elttob

"""

#Variant 1
text = input()

while text != "end":


    rev = reversed(text)
    for char in rev:
        print(char, end="")

    text = input()

#Variant 2
"""
text = input()

while text != "end":

    rev = reversed(text)
    reversed_text = "".join(rev)
    print(f"{text} = {reversed_text}")
    text = input()


"""
