"""
input1
10
170.00
6

output1
Yes! 5.00

input2
21
1570.98
3

output2
No! 997.98
"""
#!!!! #GitHub  - 100% Judge

age = int(input())
washing_price = float(input())
toy_price = int(input())

money_saved = 0
toys_count = 0
amount = 0


for birthday in range(1,age+1):

    if birthday % 2 == 0:
        amount += 10
        money_saved += amount - 1

    else:
        toys_count += 1


money_saved += toys_count * toy_price

if money_saved >= washing_price:
    print(f"Yes! {money_saved - washing_price:.2f}")
else:
    print(f"No! {washing_price - money_saved:.2f}")











