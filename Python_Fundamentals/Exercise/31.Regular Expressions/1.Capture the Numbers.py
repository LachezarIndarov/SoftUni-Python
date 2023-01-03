"""
https://regex101.com/

Input1
The300
What is that?
I think it's the 3rd movie
Let's watch it at 22:45

Output1
300 3 22 45

Input2
123a456
789b987
654c321
0

Output2
123 456 789 987 654 321 0

Input3
Let's go11!!!11!
Okey!1!

Output3
11 11 1

"""
import re

expression = r'\d+'

while True:
    text = input()

    if not text: # Ako няма текст от input - break(край на While True)
        break

    result = re.findall(expression, text)

    if len(result) > 0:
        print(' '.join(result), end=' ')# Принтирай  result с празно място (' '.join) между елементите  и на един и същи ред end=' '


"""
#Пример 1

import re
# ^Thе -  Текста трябва да започва с думата "The"
# Scary$ - Текста трябва да свършва след "Spain"
# .*Spain - Вземи цвлия текст до текста "Spain"

text = "The movie was Scary"
result = re.search(r'^The.*Scary$', text)
print(result) # match='The movie was Scary'
"""

"""
#Пример 2
import re

text = "The price of OLIVEOIL is 4 leva"

# () - всичко в тези скоби е група
# .+ - игнорирай всичко преди това и ми върни стойностите само на групите
result = re.search(r'(\b[A-Z]+\b).+(\b\d+)', text)
print(result.groups()) # Връща резултата от двете групи. (\b[A-Z]+\b) - Група 1, (\b\d+) - Група 2, --- ('OLIVEOIL', '4')
print(result.group(1)) # Връща резултата само от група 1 --- OLIVEOIL
print(result.group(2)) # Връща резултата само от група 2 --- 4

"""
"""
#Пример 3
import  re

text = 'The weather in Spain is nice'
result = re.split(r'\s', text) # split - разделяни всяка дума в текста по празно място
print(result) #['The', 'weather', 'in', 'Spain', 'is', 'nice'] - резултата е лист от стрингове
"""

"""
#Пример 4
#re.IGNORECASE

import re

text = 'MArio is Python Developer at a BioPharmacy.Mario loves ML and AI. mariO'
result = re.findall('Mario', text, re.IGNORECASE) # re.IGNORECASE - хваща всички видове съвпадения 'Mario' в текста, независимо дали са с малка или главна буква.

print(result)

"""

"""
#Пример 5
#re.X re.VERBOSE
# .+ - игнорирай всичко преди това и ми върни стойностите само на групите

import re

text = 'Mario is Python Developer at a BioPharmacy, his age is 32'
# Чрез re.VERBOSE или re.X можем да добавяме коментари в RegEx  кода, за да стане по четливо за нас и нашите колеги.
result = re.search(r'''(^\w{5}) #match 5 letters at the start
                         .+(\d{2}$) #match 2 digits at the end ''', text,re.VERBOSE)

print(result.group(1))
print(result.group(2))

"""



