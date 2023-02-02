"""
input1
7
Peter 5.20
Mark 5.50
Peter 3.20
Mark 2.50
Alex 2.00
Mark 3.46
Alex 3.0

output1
Mark -> 5.50 2.50 3.46 (avg: 3.82) Peter -> 5.20 3.20 (avg: 4.20) Alex -> 2.00 3.00 (avg: 2.50)

input2
4
Scott 4.50
Ted 3.00
Scott 5.00
Ted 3.6

output2
Ted -> 3.00 3.66 (avg: 3.33) Scott -> 4.50 5.00 (avg: 4.75)

input3
5
Lee 6.00
Lee 5.50

output3
Peter -> 4.40 (avg: 4.40) Lee -> 6.00 5.50 6.00 (avg: 5.83) Kenny -> 3.30 (avg: 3.30)
"""

def avg(values): # Function for average value
    return sum(values) / len(values)


n = int(input())
student_strings = [input() for _ in range(n)]

students_grades = {}
for student_string in student_strings:
    student,grade_string = student_string.split(' ')
    grade = float(grade_string)
    if student not in students_grades:
        students_grades[student] = []

    students_grades[student].append(grade)

for student,grades in students_grades.items():
    grades_avg = avg(grades)
    grates_formatted = ' '.join(f'{grade:.2f}' for grade in grades)
    grades_avg_formatted = f'{grades_avg:.2f}'
    print(f'{student} -> {grates_formatted} (avg: {grades_avg_formatted})')

"""
Variant2
def avg(values):
    return sum(values) / len(values)


# n = 7
# student_strings = [
#     'Peter 5.20',
#     'Mark 5.50',
#     'Peter 3.20',
#     'Mark 2.50',
#     'Alex 2.00',
#     'Mark 3.46',
#     'Alex 3.00',
# ]

n = int(input())
student_strings = [input() for _ in range(n)]

students_grades = {}

for student_string in student_strings:
    student, grade_string = student_string.split(' ')
    grade = float(grade_string)
    if student not in students_grades:
        students_grades[student] = []

    students_grades[student].append(grade)

for student, grades in students_grades.items():
    grades_avg = avg(grades)
    grades_formatted = ' '.join(f'{grade:.2f}' for grade in grades)
    grades_avg_formatted = f'{grades_avg:.2f}'
    print(f'{student} -> {grades_formatted} (avg: {grades_avg_formatted})')

"""