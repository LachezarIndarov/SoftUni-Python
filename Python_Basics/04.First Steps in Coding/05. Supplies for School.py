"""
Input1
212
20
2

Output1
5

Input2
432
15
4

Output2
7

"""


#GitHub  - 100% Judge

packages_pen = int(input())
packages_markers  = int(input())
liters_detergent = int(input())
percentage_reduction = int(input())

pen_price = 5.80
marker_price = 7.20
detergent_price = 1.20


price_sum = (packages_pen * pen_price) + (packages_markers * marker_price) + (liters_detergent * detergent_price)
price_with_discount = price_sum - (price_sum * (percentage_reduction / 100))
print(price_with_discount)





