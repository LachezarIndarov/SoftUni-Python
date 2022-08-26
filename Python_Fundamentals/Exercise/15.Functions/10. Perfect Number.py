"""
input1
6

output1
We have a perfect number!

Comments:
 1 + 2 + 3

input2
28

output2
We have a perfect number!

Comments:
1 + 2 + 4 + 7 + 14

input3
1236498

output3
It's not so perfect.
"""

def perfect_number(num):
    prop_div = []
    for n in range(1, + num):
        if num % n == 0:
            prop_div.append(n)
    if sum(prop_div) == num:
        print("We have a perfect number!")
    else:
        print("It's not so perfect.")
    return num


number = int(input())
perfect_number(number)