"""
Input1
10
11
4
8

Output1
727.09

Input2
5
10
10
1

Output2
286.52

"""
#GitHub  - 100% Judge

the_required_amount_of_nylon = int(input())
the_required_amount_of_paint = int(input())
amount_of_diluent = int(input())
hours_work = int(input())


nylon_price = 1.50
paint_price = 14.50
diluent_price = 5
bags = 0.40


sum_nylon = (the_required_amount_of_nylon + 2) * nylon_price
sum_paint = (the_required_amount_of_paint + (the_required_amount_of_paint * 10 / 100)) * paint_price
sum_diluent = amount_of_diluent * diluent_price

sum_all_products = sum_nylon + sum_paint + sum_diluent + 0.4
builder_hours_work = (sum_all_products * ( 30 / 100 )) * hours_work

all_costs = sum_all_products + builder_hours_work

print(all_costs)









