"""
Input1
5
John
5.5
John
4.5
Alice
6
Alice
3
George
5

Output1
John -> 5.00
Alice -> 4.50
George -> 5.00



Input2

5
Amanda
3.5
Amanda
4
Rob
5.5
Christian
5
Robert
6

Output2
Rob -> 5.50
Christian -> 5.00
Robert -> 6.00

"""
numbers_of_people = int(input())
dict_names_grades = {}

for i in range(numbers_of_people):
    name = input()
    grade = float(input())

    if name not in dict_names_grades:
        dict_names_grades[name] = [grade]
    else:
        dict_names_grades[name].append(grade)


[print(f"{name} -> {(sum(value) / len(value)):.2f}")

for name, value in dict_names_grades.items() if sum(value) / len(value) >= 4.5]

