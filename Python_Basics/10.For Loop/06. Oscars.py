"""
input 1
Zahari Baharov
205
4
Johnny Depp
45
Will Smith
29
Jet Lee
10
Matthew Mcconaughey
39

output1
Sorry, Zahari Baharov you need 247.5 more!

input2
Sandra Bullock
340
5
Robert De Niro
50
Julia Roberts
40.5
Daniel Day-Lewis
39.4
Nicolas Cage
29.9
Stoyanka Mutafova
33

output2
Congratulations, Sandra Bullock got a nominee for leading role with 1268.5!

"""
#!!!! #GitHub  - 100% Judge

actor = input()
initial_points = float(input())
judges_count = int(input())


points_needed = 1250.5
is_nominated = False

for judge in range(judges_count):
    judge_name = input()
    points = float(input())

    initial_points += len(judge_name) * points / 2

    if initial_points > points_needed:
        print(f"Congratulations, {actor} got a nominee for leading role with {initial_points:.1f}!")
        is_nominated = True
        break

if initial_points <= points_needed:
    print(f"Sorry, {actor} you need {points_needed - initial_points:.1f} more!")






