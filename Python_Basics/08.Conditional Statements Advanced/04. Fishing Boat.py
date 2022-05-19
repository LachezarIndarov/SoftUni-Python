"""
input1
3000
Summer
11

output1
Not enough money! You need 570.00 leva.

input2
3600
Autumn
6

output2
Not enough money! You need 180.00 leva.

"""
#GitHub  - 100% Judge

grоup_budget = int(input())
season = str(input())
number_of_fisherman = int(input())

price_boat = 0

if  season == "Spring":
    price_boat = 3000
elif season == "Summer":
    price_boat = 4200
elif season == "Autumn":
    price_boat = 4200
elif season == "Winter":
    price_boat = 2600

if number_of_fisherman <= 6:
    price_boat -= price_boat * 0.1
elif number_of_fisherman >= 7 and number_of_fisherman <= 11:
    price_boat -= price_boat * 0.15
elif number_of_fisherman >= 12:
    price_boat -= price_boat * 0.25

if number_of_fisherman % 2 == 0 and not season == "Autumn":
    price_boat -= price_boat * 0.05

if grоup_budget >= price_boat:
    print(f"Yes! You have {abs(grоup_budget - price_boat):.2f} leva left.")
elif price_boat > grоup_budget:
    print(f"Not enough money! You need {abs(grоup_budget - price_boat):.2f} leva.")



