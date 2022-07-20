"""
input1
2
PB Python
PF Python

output1
['PB Python', 'PF Python']

input2
4
Front-End
C# Web
JS Core
Programming Fundamentals

output2
['Front-End', 'C# Web', 'JS Core', 'Programming Fundamentals']

"""
number = int(input())
courses = list()

for i in range(number):
    courses.append(input())

print(courses)