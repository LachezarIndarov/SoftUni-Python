"""
input1
2-Walk the dog
1-Drink coffee
6-Dinner
5-Work
End

output1
['Drink coffee', 'Walk the dog', 'Work', 'Dinner']

input2
3-C
2-A
1-B
6-V
End

output2
['B', 'A', 'C', 'V']

"""

todo = [""for i in range(11)]

command = input()

while command != "End":
    explode = command.split("-")
    priority = int(explode[0])
    task = explode[1]
    todo[priority] = task
    command = input()

final_todo = [task for task in todo if task !=""]

print(final_todo)
