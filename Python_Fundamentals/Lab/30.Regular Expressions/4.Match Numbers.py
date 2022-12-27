"""
https://regex101.com/ - от този сайт може да си намирами нещата, който ни трябват и да ги тестваме

Input
1 -1 1s 123 s-s -123 _55_ _f 123.456 -123.456 s-1.1 s2 -1- zs-2 s-3.5 00.5

Output
1 -1 123 -123 123.456 -123.456

(^|(?<=\s)) - Проверяваме дали преди това което искъм да  match-на има нещо.

($|(?=\s)) - Или край на стринг ($) или poositive lookahead на празно място.

\s  - празно място

-?  - или има минус или няма минус

+   - един път или повече

*  -  нула или повече пъти

"""

import  re

text = input()
expression = r"(^|(?<=\s))-?([0]|[1-9][0-9]*)(\.[0-9]+)?($|(?=\s))"

matches = re.finditer(expression, text)

output = list()

for match in matches:
    output.append(match.group())

print(" ".join(output))