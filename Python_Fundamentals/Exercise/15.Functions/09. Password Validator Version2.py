"""
input1
logIn

output1
Password must be between 6 and 10 characters
Password must have at least 2 digits

input2
MyPass123

output2
Password is valid

input3
Pa$s$s

output3
Password must consist only of letters and digits
Password must have at least 2 digits
"""

def password(pas):
    list_pass = []
    digit_number = 0
    special_symbol = False
    valid_pass = True
    for i in range (len(pas)):
        list_pass.append(pas[i])
        if (ord(list_pass[i]) < 48) or (57 < ord(list_pass[i]) < 65) or (90 < ord(list_pass[i]) < 97) or (ord(list_pass[i]) > 122):
            special_symbol = True
        if 48 <= ord(list_pass[i]) <= 57:
            digit_number += 1
    if len(list_pass) > 10 or len(list_pass) < 6:
        print("Password must be between 6 and 10 characters")
        valid_pass = False
    if special_symbol:
        print("Password must consist only of letters and digits")
        valid_pass = False
    if digit_number < 2:
        print("Password must have at least 2 digits")
        valid_pass = False
    if valid_pass:
        print("Password is valid")

input_str = input()
password(input_str)
