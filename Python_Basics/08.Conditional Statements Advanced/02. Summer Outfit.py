"""
input1
16
Morning

output1
It's 16 degrees, get your Sweatshirt and Sneakers.

input2
22
Afternoon

output2
It's 22 degrees, get your T-Shirt and Sandals.
"""
#GitHub  - 100% Judge

degrees = int(input())
time_of_day = str(input())
outfiet = ""
shoes = ""

if time_of_day == "Morning":
    if 10 <= degrees <= 18:
        outfiet = "Sweatshirt"
        shoes = "Sneakers"

    elif 18 < degrees <= 24:
        outfiet = "Shirt"
        shoes = "Moccasins"

    else:
        outfiet = "T-Shirt"
        shoes = "Sandals"

if time_of_day == "Afternoon":
    if 10 <= degrees <= 18:
        outfiet = "Shirt"
        shoes = "Moccasins"

    elif 18 < degrees <= 24:
        outfiet = "T-Shirt"
        shoes = "Sandals"

    else:
        outfiet = "Swim Suit"
        shoes = "Barefoot"

if time_of_day == "Evening":
    if 10 <= degrees <= 18:
        outfiet = "Shirt"
        shoes = "Moccasins"

    elif 18 < degrees <= 24:
        outfiet = "Shirt"
        shoes = "Moccasins"

    else:
        outfiet = "Shirt"
        shoes = "Moccasins"

print(f" It's {degrees} degrees, get your {outfiet} and {shoes}.")



