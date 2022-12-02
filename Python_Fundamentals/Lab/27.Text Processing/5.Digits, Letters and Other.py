"""
Input1
Agd#53Dfg^&4F53

Output1
53453
AgdDfgF
#^&

"""

# Variant 1
text = input()
digits = ""
letters = ""
symbols = ""

for ch in text:
    if ch.isdigit():
        digits += ch

    elif ch.isupper() or ch.islower():
        letters += ch

    else:
        symbols += ch

print(digits)
print(letters)
print(symbols)

""""
# Variant 2

text = input()
digits = ""
letters = ""
symbols = ""

for ch in text:
    if ch.isdigit():
        digits += ch


    elif ch.isalpha(): 
        letters += ch

    else:
        symbols += ch

print(digits)
print(letters)
print(symbols)


"""