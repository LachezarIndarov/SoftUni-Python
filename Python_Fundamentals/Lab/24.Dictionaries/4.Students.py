"""
input1
Peter:123:programming basics
John:5622:fundamentals
Maya:89:fundamentals
Lilly:633:fundamentals
fundamentals

output1
John - 5622
Maya - 89
Lilly - 633

input2
Alex:6:programming basics
Maria:7:programming basics
Kaloyan:9:advanced
Todor:10:fundamentals
programming_basics

output2
Alex - 6
Maria - 7


"""

text = input()
courses = {}

while ":" in text:

    data = text.split(":")
    name = data[0]
    id = data[1]
    course = data[2]

    if course not in courses.keys():
        courses[course] = {}

    courses[course][id] = name



    text = input()


text = text.replace("_"," ")

for id in courses[text]:
    print(f"{courses[text][id]} - {id}")


