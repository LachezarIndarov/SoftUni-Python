"""
input1
water
5

output1
5.00

input2
coffee
2

output2
3.00

"""
def calc_price(product,quantity):
    if product == "coffee":
        return quantity * 1.5
    elif product == "coke":
        return quantity * 1.4
    elif product == "water":
        return quantity * 1.00
    elif product == "snacks":
        return quantity * 2.0

product = input()
quantity = int(input())

final_price = (calc_price(product,quantity))

print(f"{final_price:.2f}")
