"""
input1
5.12
32.05
15
150

output1
Profit: 170.85 BGN, the gift has been purchased.

input2
2.10
17.50
20.20
148.50

output2
Insufficient money: 70.70 BGN.

input3
15.20
200.00
7.30
1500.12

output3
Insufficient money: 431.42 BGN.

"""
Teresa_pocket_money_per_day = float(input())
the_money_she_earns_per_day_from_sales = float(input())
Teresa_expenses_for_the_entire_period = float(input())
the_price_of_the_gift = float(input())

days = 5

saved_money = days * Teresa_pocket_money_per_day
money_earned = days * the_money_she_earns_per_day_from_sales
all_saved_money = saved_money + money_earned
we_subtract_the_costs = all_saved_money - Teresa_expenses_for_the_entire_period

if we_subtract_the_costs >= the_price_of_the_gift:
    print(f"Profit: {we_subtract_the_costs:.2f} BGN, the gift has been purchased." )
else:
    print(f"Insufficient money: {the_price_of_the_gift - we_subtract_the_costs:.2f} BGN.")

