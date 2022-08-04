"""
input1
3.33

output1
Poor

input2
4.50

output2
Very Good

input3
2.99

output3
Fail

"""
def grade_text(grade_number):

    if grade_number < 3:
        return "Fail"
    elif grade_number < 3.5:
        return "Poor"
    elif grade_number < 4.5:
        return "Good"
    elif grade_number < 5.5:
        return "Very Good"
    elif grade_number >= 5.5:
        return "Excellent"

current_grade = float(input())

print(grade_text(current_grade))


