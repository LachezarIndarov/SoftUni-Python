"""
Input1

Programming Fundamentals : John Smith
Programming Fundamentals : Linda Johnson
JS Core : Will Wilson
Java Advanced : Harrison White
end

Output1
Programming Fundamentals: 2
-- John Smith
-- Linda Johnson
JS Core: 1
-- Will Wilson
Java Advanced: 1
-- Harrison White


Input2

Algorithms : Jay Moore
Programming Basics : Martin Taylor
Python Fundamentals : John Anderson
Python Fundamentals : Andrew Robinson
Algorithms : Bob Jackson
Python Fundamentals : Clark Lewis
end

Output2
Algorithms: 2
-- Jay Moore
-- Bob Jackson
Programming Basics: 1
-- Martin Taylor
Python Fundamentals: 3
-- John Anderson
-- Andrew Robinson
-- Clark Lewis


"""

dict = {}


while True:
    command = input()

    if command == "end":
        break


    course, student = command.split(" : ")


    if course not in dict:
        dict[course] = []


    dict[course].append(student)


for course, students in dict.items():
    print(f"{course}: {len(students)}")
    for student in students:
        print(f"-- {student}")










