"""
input1
3
Money
6
Story
4
Spring Time
5
Bus
6
Enough

output1
Average score: 5.25
Number of problems: 4
Last problem: Bus

input2
2
Income
3
Game Info
6
Best Player
4

output2
You need a break, 2 poor grades.

"""
#GitHub  - 100% Judge

failed_threshold = int(input())

failed_times = 0
solved_problems_count = 0
grades_sum = 0
last_problem = ""
has_failed = True


while failed_times < failed_threshold:
    problem_name = input()
    if problem_name == "Enough":
        has_failed = False
        break

    grade = int(input())
    if grade <= 4:
        failed_times += 1
    grades_sum += grade
    solved_problems_count += 1
    last_problem = problem_name

if has_failed:
    print(f" You need a break, {failed_threshold} poor grades.")
else:
    print(f"Average score: {grades_sum / solved_problems_count:.2f}")
    print(f"Number of problems: {solved_problems_count}")
    print(f"Last problem: {last_problem}")