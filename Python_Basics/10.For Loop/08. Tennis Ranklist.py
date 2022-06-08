"""
input1
5
1400
F
SF
W
W
SF

output1
Final points: 8040
Average points: 1328
40.00%


input2
4
750
SF
W
SF
W

output2
Final points: 6190
Average points: 1360
50.00%

input3
7
1200
SF
F
W
F
W
SF
W

output3
Final points: 11040
Average points: 1405
42.86%

"""
#GitHub  - 100% Judge

import math

tournaments_counts = int(input())
initial_points = int(input())

w = 2000
f = 1200
sf = 720

points = 0
winner = 0

for Grigor_Dimitrov in range(tournaments_counts):
    stage = input()

    if stage == "W":
        points += w
        winner += 1

    elif stage == "F":
        points += f

    elif stage == "SF":
        points += sf

average_points = math.floor(points / tournaments_counts)
win_percent = winner / tournaments_counts * 100
final_points = initial_points + points

print(f"Final points: {final_points}")
print(f"Average points: {(average_points)}")
print (f"{win_percent:.2f}%")