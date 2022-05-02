"""
input1
365

output1
811.76

input2
550

output2
1223.2

"""

#GitHub  - 100% Judge

YearTaxBasketTraining = int(input())

basketball_shoes_price = (YearTaxBasketTraining - (YearTaxBasketTraining * 40 / 100))
price_for_basketball_equipment = (basketball_shoes_price - (basketball_shoes_price * 20/100))
ball_price = (price_for_basketball_equipment * (  25 / 100))
accessories_price = (ball_price * ( 20/100))

full_price_all = YearTaxBasketTraining + basketball_shoes_price + price_for_basketball_equipment + ball_price + accessories_price

print(full_price_all)


