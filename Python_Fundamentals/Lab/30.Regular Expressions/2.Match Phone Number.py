"""
https://regex101.com/

        Input
+359 2 222 2222,359-2-222-2222, +359/2/222/2222, +359-2 222 2222 +359 2-222-2222,+359-2-222-222, +359-2-222-22222 +359-2-222-2222

        Output
+359 2 222 2222, +359-2-222-2222

"""
import re

text = input()

matches = re.findall(r"\+359 2 \d{3} \d{4}\b|\+359-2-\d{3}-\d{4}\b", text)

print(", ".join(matches))


"""
Двата варианта са тествани в Judge  и работят 100/100
Варинт 2 

# re.finditer - ни връща итератор, който има мачовете(match), на който имат в себе си съдържанието
# \1 - Връща ни група 1

import re

text = input()

# ([ -]) - след +359 ми търси по празно място или тире
matches = re.finditer(r"\+359([ -])2\1\d{3}\1\d{4}\b", text)

output = list()
for match in matches:
    output.append(match.group())
    
print(", ".join(output))


"""