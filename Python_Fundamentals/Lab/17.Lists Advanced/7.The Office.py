"""
input1
1 2 3 4 2 1
3

output1
Score: 2/6. Employees are not happy!

Comment:

After the mapping:
3 6 9 12 6 3
After the filtration:
9 12
2/6 people are happy, so the overall happiness is bad


input2
2 3 2 1 3 3
4

output2
Score: 3/6. Employees are happy!

Comment:

After the mapping:
3 6 9 12 6 3
After the filtration:
9 12
2/6 people are happy, so the overall happiness is bad


"""

employees_string = input().split(" ")
employees = list(map(int,employees_string))

factor = int(input())


happy_employees = list(filter(lambda shtastie: shtastie >= sum(employees) / len(employees), employees ))

if len(happy_employees) >= len(employees) / 2:
    print(f"Score: {len(happy_employees)}/{len(employees)}. Employees are happy!")

else:
     print(f"Score: {len(happy_employees)}/{len(employees)}. Employees are not happy!")