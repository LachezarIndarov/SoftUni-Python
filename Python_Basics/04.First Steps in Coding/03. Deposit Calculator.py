"""
Input1
200
3
5.7

Output1
202.85

Input2
2350
6
7

Output2
2432.25
"""

#GitHub  - 100% Judge

deposited_amount = float(input())
term_of_the_deposit = int(input())
annual_interest_rate = float(input())


amount = deposited_amount + term_of_the_deposit * ((deposited_amount * annual_interest_rate / 100) / 12)

print(amount)

