"""
input1
40.8
20
25
30
50
10

output1
Yes! 418.20 lv left.

input2
320
8
2
5
5
1

output2
Not enough money! 238.73 lv needed.

"""
#GitHub  - 100% Judge

price_of_the_trip = float(input())
number_of_puzzles = int(input())
number_of_dolls = int(input())
number_of_teddy_bears = int(input())
number_of_minions = int(input())
number_of_trucks  = int(input())

puzzle_price = 2.60
doll_price = 3
teddy_bear_price = 4.10
minion_price = 8.20
truck = 2
discount = 0

sum =  (number_of_puzzles * puzzle_price) + (number_of_dolls * doll_price) + (number_of_teddy_bears * teddy_bear_price) + (number_of_minions * minion_price) + (number_of_trucks * truck)

numbers_of_toys = number_of_puzzles + number_of_dolls + number_of_teddy_bears + number_of_minions + number_of_trucks

if numbers_of_toys >= 50:
    discount =  sum * 0.25
    
final_price = sum - discount
rent = final_price * 0.1
profit = final_price - rent

remaining_money = profit - price_of_the_trip


if profit >= price_of_the_trip:
    print(f"Yes! {remaining_money:.2f} lv left.")
else:
    print(f"Not enough money! {abs(remaining_money) :.2f} lv needed.")


