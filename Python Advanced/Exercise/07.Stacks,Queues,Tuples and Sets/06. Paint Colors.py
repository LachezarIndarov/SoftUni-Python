"""
input1
d yel blu e low redd

output1
['yellow', 'blue', 'red']

Comments:
First, we take "d" and "redd". After combining those substrings, we don't get any of the needed colors, so we remove the last characters from both substrings and return them in the middle of the original string, and it becomes "yel blu red e low".
After that, we take "yel" and "low" so the first color we add to our list is yellow, and the string we are searching in looks as follows: "blu red e"
Then we take "blu" and "e", and since this color is one of the searched ones (blue), we add it to our collection, and the state of the string is now "red".
We should take the last substring and check if it matches some of the colors, and since it does, we add it (red) to our colors collection.
Finally, we print all the colors found: yellow, blue, and red in the format shown above.

input2
r ue nge ora bl ed

output2
['red', 'blue']

Comments:
We don't keep orange because we don't have yellow in the final list with colors (combining red and yellow gives us orange).

input3
re ple blu pop e pur d

output3
['red', 'purple', 'blue']

"""

from collections import deque

words = deque(input().split())

primary_colors = {"red", "yellow", "blue"}
secondary_colors = {"orange", "purple", "green"}

collected_colors = []

while words:
    # red + d -> redd
    # red + '' -> red
    left = words.popleft()
    right = words.pop() if words else ''

    result = left + right
    if result in primary_colors or result in secondary_colors:
        collected_colors.append(result)
        continue

    result = right + left
    if result in primary_colors or result in secondary_colors:
        collected_colors.append(result)
        continue

    left = left[:-1]
    right = right[:-1]

    if left:
        words.insert(len(words) // 2, left)
    if right:
        words.insert(len(words) // 2, right)

result = []

forming_colors = {

    'orange': ['red', 'yellow'],
    'purple': ['red', 'blue'],
    'green': ['yellow', 'blue']
}

for color in collected_colors:
    if color in primary_colors:
        result.append(color)
        continue

    is_collected = True
    for helper_color in forming_colors[color]:
        if helper_color not in collected_colors:
            is_collected = False
            break

    if is_collected:
        result.append(color)

print(result)