"""
input1
Premiere
10
12

output1
1440.00 leva

input2
Normal
21
13

output2
2047.50 leva

input3
Discount
12
30

output3
1800.00 leva

"""
#GitHub  - 100% Judge

screening_type = input()
rows = int(input())
columns = int(input())


income = 0

cinema_capacity = rows * columns

if screening_type == "Premiere":
    income = cinema_capacity * 12
elif screening_type == "Normal":
    income = cinema_capacity * 7.50
elif screening_type == "Discount":
    income = cinema_capacity * 5

print(f"{income:.2f} leva")

