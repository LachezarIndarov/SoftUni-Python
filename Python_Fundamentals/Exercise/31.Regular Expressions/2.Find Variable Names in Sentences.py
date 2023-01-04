"""
Input1                                                                          Output1
The _id and _age variables are both integers.                                   id,age

Input2                                                                          Output2
Calculate the _area of the _perfectRectangle object.                       area,perfectRectangle

Input3                                                                          Output3
__invalidVariable _evenMoreInvalidVariable_ _validVariable	                  validVariable

"""

# "+" - един или повече символа, без + обикновено взима само първата буква.
#\b_[a-zA-Z0-9]+\b     - \b_ - взима думите започващи с  долна черта,[a-zA-Z0-9] - Взима първите символи на думите ако започват с a-zA-Z0-9, + - взима и останалите букви след първата буква

import re

text = input()

expression = r'\b_[a-zA-Z0-9]+\b'

result = re.findall(expression, text)

word_list = []

for word in result:
    # Тук добавяме тази проверка (word[1:]) за да премахмен първото долно тире по условие в листа, като то е с индекс 0 а ние разпечатваме от  индекс 1 нататък
    word_list.append(word[1:])

#Тук чрез ".join" разделяме стринговете в print-a със запетая ','
print(','.join(word_list))