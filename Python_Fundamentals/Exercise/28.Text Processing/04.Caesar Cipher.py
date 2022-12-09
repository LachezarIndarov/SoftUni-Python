""""
Input1                                  Output1
Programming is cool!                    Surjudpplqj#lv#frro$

Input2                                  Output2
One year has 365 days.                  Rqh#|hdu#kdv#698#gd|v1

"""

def caesar_cipher(text):


    result = [chr(ord(ch) + 3) for ch in text]
    print(''.join(result))

text = input()
caesar_cipher(text)
