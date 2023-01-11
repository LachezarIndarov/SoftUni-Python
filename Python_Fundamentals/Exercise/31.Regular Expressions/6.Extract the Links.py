"""
Input1
Join WebStars now for free, at www.web-stars.com
You can also support our partners:
Internet - www.internet.com
WebSpiders - www.webspiders101.com
Sentinel - www.sentinel.-ko

Output1
www.web-stars.com
www.internet.com
www.webspiders101.com

Input2
Need information about cheap hotels in London?
You can check us at www.london-hotels.co.uk !
We provide the best services in London.
Here are some reviews in some blogs:
London Hotels are awesome! - www.indigo.bloggers.com
I am very satisfied with their services - ww.ivan.bg
Best Hotel Services! - www.rebel21.sedecrem.moc

Output2
www.london-hotels.co.uk
www.indigo.bloggers.com
www.rebel21.sedecrem.moc

"""

import re

text = input()

expression = r'(www\.)([a-zA-Z0-9-]+)(\.[a-z]+)+'

result  = re.findall(expression, text)

word_list = []

for i in result:
    word_list.append(i)

print(word_list)


#expression = r'/(www\.)([a-zA-Z0-9-]+)(\.[a-z]+)+/g'

# test (www\.)([a-zA-Z0-9-]+)(\.[a-z]+)+

"""
import re

text = input()

expression = r'\b_[a-zA-Z0-9]+\b'

result = re.findall(expression, text)

word_list = []

for word in result:
    # Тук добавяме тази проверка (word[1:]) за да премахмен първото долно тире по условие в листа, като то е с индекс 0 а ние разпечатваме от  индекс 1 нататък
    word_list.append(word[1:])

print(','.join(word_list))

"""