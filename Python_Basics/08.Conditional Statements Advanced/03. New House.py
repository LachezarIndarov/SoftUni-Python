"""
input1
Roses
55
250

output1
Not enough money, you need 25.00 leva more.

input2
Tulips
88
260

output2
Hey, you have a great garden with 88 Tulips and 50.56 leva left.

input3
Narcissus
119
360

output3
Not enough money, you need 50.55 leva more.
"""
#GitHub  - 100% Judge

type_flowers = str(input())
amount_flowers = int(input())
budget = int(input())

rose_price = 5
dahlia_price = 3.80
tulip_price = 2.80
narcissus_price = 3
gladiolus_price = 2.5


price = 0

if type_flowers == "Roses":
    price = (rose_price * amount_flowers)
    if amount_flowers > 80:
        price -= price * 0.1

elif type_flowers == "Dahlias":
    price = (dahlia_price * amount_flowers)
    if amount_flowers > 90:
        price -= price * 0.15

elif type_flowers == "Tulips":
    price = (tulip_price * amount_flowers)
    if amount_flowers > 80:
        price -= price * 0.15

elif type_flowers == "Narcissus":
    price = (narcissus_price * amount_flowers)
    if amount_flowers < 120:
        price += price * 0.15

elif type_flowers == "Gladiolus":
    price = (gladiolus_price * amount_flowers)
    if amount_flowers < 80:
        price += price * 0.2


if price > budget:
    print(f"Not enough money, you need {abs(price - budget):.2f} leva more.")
elif budget >= price:
    print(f"Hey, you have a great garden with {amount_flowers} {type_flowers} and {abs(budget - price):.2f} leva left.")