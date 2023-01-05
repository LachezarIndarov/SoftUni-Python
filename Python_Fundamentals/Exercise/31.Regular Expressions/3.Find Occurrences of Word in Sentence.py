"""
Input1                                                                                          Output1
The waterfall was so high, that the child couldn't see its peak.                                    2
the

Input2                                                                                          Output2
How do you plan on achieving that? How? How can you even think of that?                            3
how

Input3                                                                                           Output3
There was one. Therefore I bought it. I wouldn't buy it otherwise.                                  1
there


"""
import re

text = input()
special_word = input()

# Тук се вижда, че в RegEx  може чрез "rf" да се вкарва и променливи и да се сравнява по тях
expression = rf'\b{special_word}\b'

# re.IGNORECASE - хваща всички видове съвпадения 'the' в текста, независимо дали са с малка или главна буква.
result  = re.findall(expression, text, re.IGNORECASE)

print(len(result))#Тук добавяме  "len" за да ни преброй колко пъти се повтаря тази дума като бройка в текста. Ако го няма "len" ще даде грешка, защото ще изпринтира само вътре в листа резултата вместо брой 2 пъти.Пример: без len ['The', 'the']

