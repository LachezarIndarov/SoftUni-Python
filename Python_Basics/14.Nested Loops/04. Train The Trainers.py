"""
input1
2
While-Loop
6.00
5.50
For-Loop
5.84
5.66
Finish

output1
While-Loop - 5.75.
For-Loop - 5.75.
Student's final assessment is 5.75.

input2
3
Arrays
4.53
5.23
5.00
Lists
5.83
6.00
5.42
Finish

output2
Arrays - 4.92.
Lists - 5.75.
Student's final assessment is 5.34.

input3
2
Objects and Classes
5.77
4.23
Dictionaries
4.62
5.02
RegEx
2.88
3.42
Finish


output3
Objects and Classes - 5.00.
Dictionaries - 4.82.
RegEx - 3.15.
Student's final assessment is 4.32.

"""
#!!!!!!
number_of_people_on_the_jury = int(input())
name_of_the_presentation = input()
average_grade_sum = 0
the_number_of_presentations = 0

while name_of_the_presentation != "Finish":
    average_grade = 0


    for n in range(number_of_people_on_the_jury):

        average_grade += float(input())

    average_grade /= number_of_people_on_the_jury
    print(f"{name_of_the_presentation} - {average_grade:.2f}.")

    average_grade_sum += average_grade
    the_number_of_presentations += 1




    name_of_the_presentation = input()

average_grade_sum /= the_number_of_presentations
print(f"Student's final assessment is {average_grade_sum:.2f}.")



