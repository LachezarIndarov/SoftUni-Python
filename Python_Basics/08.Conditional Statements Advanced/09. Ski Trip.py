"""
input1
14
apartment
positive

output1
264.06

input2
30
president apartment
negative

output2
730.80

input3
12
room for one person
positive

output3
247.50

input4
2
apartment
positive

output4
21.88
"""
#GitHub  - 100% Judge

days_for_stay = int(input())
type_of_room = str(input())
evaluation = str(input())

full_price = 0
price_room = 18
price_apartment = 25
price_president_apartment = 35
days_for_stay = days_for_stay - 1
price1 = days_for_stay * price_room
price2 = days_for_stay * price_apartment
price3 = days_for_stay * price_president_apartment

if type_of_room == "room for one person" and evaluation == "positive"  and days_for_stay > 1:

    price1 = days_for_stay * price_room
    price1 += price1 * 0.25
    full_price = price1

elif type_of_room == "room for one person" and evaluation == "negative"  and days_for_stay > 1:
    price1 = days_for_stay * price_room
    price1 -= price1 * 0.1
    full_price = price1

elif type_of_room == "apartment" and evaluation == "positive" and days_for_stay < 10:
    price2 = days_for_stay * price_apartment
    price2 -= price2 * 0.30
    price2 += price2 * 0.25
    full_price = price2

elif type_of_room == "apartment" and evaluation == "negative" and days_for_stay < 10:
    price2 = days_for_stay * price_apartment
    price2 -= price2 * 0.30
    price2 -= price2 * 0.1
    full_price = price2


elif type_of_room == "apartment" and evaluation == "positive" and (days_for_stay >= 10 and days_for_stay <= 15):
    price2 = days_for_stay * price_apartment
    price2 -= price2 * 0.35
    price2 += price2 * 0.25
    full_price = price2

elif type_of_room == "apartment" and evaluation == "negative" and (days_for_stay >= 10 and days_for_stay <= 15):
    price2 = days_for_stay * price_apartment
    price2 -= price2 * 0.35
    price2 -= price2 * 0.1
    full_price = price2

elif type_of_room == "apartment"and evaluation == "positive" and days_for_stay > 15:
    price2 = days_for_stay * price_apartment
    price2 -= price2 * 0.5
    price2 += price2 * 0.25
    full_price = price2

elif type_of_room == "apartment"and evaluation == "negative" and days_for_stay > 15:
    price2 = days_for_stay * price_apartment
    price2 -= price2 * 0.5
    price2 -= price2 * 0.1
    full_price = price2


elif type_of_room == "president apartment" and evaluation == "positive" and days_for_stay < 10:
    price3 = days_for_stay * price_president_apartment
    price3 -= price3 * 0.1
    price3 += price3 * 0.25
    full_price = price3

elif type_of_room == "president apartment" and evaluation == "negative" and days_for_stay < 10:
    price3 = days_for_stay * price_president_apartment
    price3 -= price3 * 0.1
    price3 -= price3 * 0.1
    full_price = price3

elif type_of_room == "president apartment" and evaluation == "positive" and (days_for_stay >= 10 and days_for_stay <= 15):
    price3 = days_for_stay * price_president_apartment
    price3 -= price3 * 0.15
    price3 += price3 * 0.25
    full_price = price3
elif type_of_room == "president apartment" and evaluation == "negative" and (days_for_stay >= 10 and days_for_stay <= 15):
    price3 = days_for_stay * price_president_apartment
    price3 -= price3 * 0.15
    price3 -= price3 * 0.1
    full_price = price3
elif type_of_room == "president apartment" and evaluation == "positive" and  days_for_stay > 15:
    price3 = days_for_stay * price_president_apartment
    price3 -= price3 * 0.20
    price3 += price3 * 0.25
    full_price = price3
elif type_of_room == "president apartment" and evaluation == "negative" and  days_for_stay > 15:
    price3 = days_for_stay * price_president_apartment
    price3 -= price3 * 0.20
    price3 -= price3 * 0.1
    full_price = price3

print(f"{full_price:.2f}")







