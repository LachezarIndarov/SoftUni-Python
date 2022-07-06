"""
input1
2
10
3
10
10
11
20
2
20
10

output2
Good job! Average gold per day: 10.33.
You need 5.00 gold.

input2
1
5
3
10
1
3

output2
You need 0.33 gold.

"""

number_locations = int(input())

for i in range (0, number_locations):
    expecting_gold = float(input())
    days = int(input())
    sum_gold = 0
    for j in range (0, days):
        income_gold = float(input())
        sum_gold += income_gold
    average_income = sum_gold/days
    if average_income >= expecting_gold:
        print(f"Good job! Average gold per day: {average_income:.2f}.")
    else:
        print(f"You need {expecting_gold-average_income:.2f} gold.")
