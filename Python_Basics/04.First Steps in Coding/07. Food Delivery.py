"""
input1
2
4
3

output1
116.2


input2
9
2
3

output2
173.38
"""
#GitHub  - 100% Judge

amount_chickens_menu = int(input())
amount_fish_menu = int(input())
amount_vegetarian_menu = int(input())

chickens_price = 10.35
fish_price = 12.40
vegetarian_price = 8.15
delivery = 2.50

chickens_menu_price = amount_chickens_menu * chickens_price
fish_menu_price = amount_fish_menu * fish_price
vegetarian_menu_price = amount_vegetarian_menu * vegetarian_price

all_price_menus = chickens_menu_price + fish_menu_price + vegetarian_menu_price
desert_price = (all_price_menus * (20/100))

full_price = all_price_menus + desert_price + delivery

print(full_price)


