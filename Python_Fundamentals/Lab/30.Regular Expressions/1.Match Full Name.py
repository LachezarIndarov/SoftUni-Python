"""
https://regex101.com/ - от този сайт може да си намирами нещата, който ни трябват и да ги тестваме

Input                                                                                                                Output
Peter Smith, peter smith, Peter smith, peter Smith, PEter Smith, Peter SmIth, Lily Everett                  Peter Smith Lily Everett

Output
Peter Smith Lily Everett
"""


import re

text = input()


matches = re.findall(r"\b[A-Z][a-z]+ [A-Z][a-z]+\b", text)

print(" ".join(matches))