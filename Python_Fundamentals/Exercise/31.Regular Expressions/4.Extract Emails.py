"""
https://regex101.com/

Input1                                                          Output1
Please contact us at: support@github.com.                   support@github.com

Input2
Just send email to s.miller@mit.edu and j.hopking@york.ac.uk for more information.

Output2
s.miller@mit.edu
j.hopking@york.ac.uk

Input3
Many users @ SoftUni confuse email addresses. We @ Softuni.BG provide high-quality training @ home or @ class. –- steve.parker@softuni.de.

Output3
steve.parker@softuni.de

"""


import re

text = input()
user_pattern = r'( |^)[a-zA-Z0-9]+((\.|\-|_)[a-zA-Z0-9]+)*'
host_pattern = r'[a-zA-Z]+(-[a-zA-Z]+)*(\.[a-zA-Z]+(-[a-zA-Z]+)*)+'

pattern = rf'{user_pattern}@{host_pattern}'

emails = re.finditer(pattern, text)
for email in emails:
    print(email[0])