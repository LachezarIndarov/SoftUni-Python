"""
input1
0.01
1
10
20
20

output1
Avtonom should pay 23.91 BGN.

input2
0.05
1.20
40
19.99
20

output2
Avtonom should pay 38.72 BGN.

input3
0.02
0.50
18
21
50

output3
Avtonom should pay 18.28 BGN.


"""

page_price = float(input())
cover_price = float(input())
percentage_for_paper = int(input())
designer_payment = float(input())
percentage_of_the_total_amount_due = int(input())

pages = 899
covers = 2


initial_amount_to_print = (page_price * pages) + (cover_price * covers)


initial_amount_to_print -= initial_amount_to_print * (percentage_for_paper / 100) 
initial_amount_to_print += designer_payment

initial_amount_to_print -= initial_amount_to_print * (percentage_of_the_total_amount_due / 100) 




print(f"Avtonom should pay {initial_amount_to_print:.2f} BGN.")





