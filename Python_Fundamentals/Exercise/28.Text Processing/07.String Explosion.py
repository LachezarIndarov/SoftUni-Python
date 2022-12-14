
"""
Input                                       Output

abv>1>1>2>2asdasd                           abv>>>>dasd

"""

text = input()
new_text = list()
strength = 0

for ch in text:
    if ch.isdigit():
        strength += int(ch)
        strength -= 1
        continue
    else:
        if strength < 1:
            new_text.append(ch)
        else:
            if ch == ">":
                new_text.append(ch)
            else:
                strength -= 1
                continue
print("".join(new_text))


"""
Comments:

1st explosion is at index 3, with a strength of 1. We delete only the digit after the explosion character. The string will look like this: abv>>1>2>2asdasd
2nd explosion is with strength one, and the string transforms to this: abv>>>2>2asdasd
3rd explosion is now with a strength of 2. We delete the digit, and we find another explosion. At this point, the string looks like this: abv>>>>2asdasd. 
4th explosion is with strength 2. We have 1 strength left from the previous explosion, and we add the strength of the current explosion to what is left, which adds up to a total strength of 3. We delete the next three characters, and we receive the string abv>>>>dasd 
We do not have any more explosions, and we print the result: abv>>>>dasd

"""