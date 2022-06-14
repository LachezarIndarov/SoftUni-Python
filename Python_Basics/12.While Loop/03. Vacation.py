"""
input1
2000
1000
spend
1200
save
2000

output1
You saved the money for 2 days.

input2
110
60
spend
10
spend
10
spend
10
spend
10
spend
10

output2
You can't save the money.
5

input3
250
150
spend
50
spend
50
save
100
save
100

output3
You saved the money for 4 days.
"""
#GitHub  - 100% Judge

needed_money_for_the_trip = float(input())
money_on_hand = float(input())

days_counter = 0
spending_counter = 0

while money_on_hand < needed_money_for_the_trip and spending_counter < 5:
    command = input()
    money = float(input())
    days_counter += 1
    if command == "save":
        money_on_hand += money
        spending_counter = 0
    elif command == "spend":
        money_on_hand -= money
        spending_counter += 1
        if money_on_hand < 0:
           money_on_hand = 0

if spending_counter == 5:
    print(" You can't save the money.")
    print(days_counter)

if money_on_hand >= needed_money_for_the_trip:
    print(f"You saved the money for {days_counter} days.")

