"""
input1
10
3.00
2.99
5.68
3.01
4
4
6.00
4.50
2.44
5

output1
Top students: 30.00%
Between 4.00 and 4.99: 30.00%
Between 3.00 and 3.99: 20.00%
Fail: 20.00%
Average: 4.06

input2
6
2
3
4
5
6
2.2

output2
Top students: 33.33%
Between 4.00 and 4.99: 16.67%
Between 3.00 and 3.99: 16.67%
Fail: 33.33%
Average: 3.70

"""
number_of_students_exam = int(input())

top_students = 0
good_students = 0
mediocre_students = 0
fail_students = 0
average_success = 0


for i in range(number_of_students_exam):
    rating = float(input())

    if rating > 4.99:
        top_students += 1
        average_success += rating
    elif rating >= 4.00 and rating <= 4.99:
            good_students += 1
            average_success += rating
    elif rating >= 3 and rating <= 3.99:
         mediocre_students += 1
         average_success += rating
    elif rating < 3:
        fail_students += 1
        average_success += rating


group_top = (top_students / number_of_students_exam) * 100      
print(f"Top students: {group_top:.2f}%")
group_good = (good_students / number_of_students_exam ) * 100   
print(f"Between 4.00 and 4.99: {group_good:.2f}%")
group_mediocre = (mediocre_students / number_of_students_exam) * 100 
print(f"Between 3.00 and 3.99: {group_mediocre:.2f}%")
group_fail = (fail_students / number_of_students_exam) * 100    
print(f"Fail: {group_fail:.2f}%")

average_success_full = average_success / number_of_students_exam
print(f"Average: {average_success_full:.2f}")


