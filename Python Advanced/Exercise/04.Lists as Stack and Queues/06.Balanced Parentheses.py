"""
input1
{[()]}

output1
YES

input2
{[(])}

output2
NO

input3
{{[[(())]]}}

output3
YES

"""

expression = input()

opening_brackets = []

pairs = { '(': ')', '[': ']', '{': '}' }

balanced = True
for ch in expression:
    if ch in '([{':
        opening_brackets.append(ch)
    elif not opening_brackets:
        balanced = False
    else:
        last_opening_bracket = opening_brackets.pop()
        if pairs[last_opening_bracket] != ch:
            balanced = False

    if not balanced:
        break
if not balanced or opening_brackets:
    print("NO")
else:
    print("YES")

