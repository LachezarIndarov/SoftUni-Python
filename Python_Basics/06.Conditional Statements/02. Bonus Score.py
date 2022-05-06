"""
input1
20

output1
6
26

input2
175

output2
37.0
212.0

input3
2703

output3
270.3
2973.3

"""

number = int(input())

bonus = 0

if number <= 100:
    bonus = 5

elif number <= 1000:
    bonus = number * (20/100)
else:
    bonus = number * (10/100)


if number % 2 == 0:
    bonus += 1
elif number % 10 == 5:
    bonus += 2


print(bonus)
print(bonus + number)






    #if number % 2 == 0:
     #   print('even')
    #else:
     #   print('odd')