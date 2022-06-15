"""
input1
1000
1500
2000
6500

output1
Goal reached! Good job!
1000 steps over the goal!

input2
1500
300
2500
3000
Going home
200

output2
2500 more steps to reach goal.

input3
1500
3000
250
1548
2000
Going home
2000

output3
Goal reached! Good job!
298 steps over the goal!

input4
125
250
4000
30
2678
4682

output4
Goal reached! Good job!
1765 steps over the goal!

"""
#!!!! GitHub  - 100% Judge

goal = 10000
number_of_steps = 0
TestWhile = True


while TestWhile:
    steps = input()
    if steps == 'Going home':
        steps_going_home = int(input())
        number_of_steps += steps_going_home
        if number_of_steps >= goal:
            print(f"Goal reached! Good job! ")
            print(f"{number_of_steps - goal} steps over the goal!")
        else:
            print(f"{goal - number_of_steps} more steps to reach goal.")
        break
    number_of_steps += int(steps)

    if number_of_steps >= goal:
        print(f"Goal reached! Good job!")
        print(f"{number_of_steps - goal} steps over the goal!")
        break




