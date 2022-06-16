"""
input1
1.23

output1
4

input2
2

output2
1

input3
0.56

output3
3

input4
2.73

output4
5

"""

number_of_coins = 0
sum = float(input())

while sum > 0:

    if sum >= 2:
        sum -= 2
        sum=round(sum,2) 

        number_of_coins += 1

    elif sum >= 1:
        sum -= 1
        sum=round(sum,2) 
        
        number_of_coins += 1

    elif sum >= 0.5:
        sum -= 0.5
        sum=round(sum,2) 

        number_of_coins += 1

    elif sum >= 0.2:
        sum -= 0.2
        sum=round(sum,2) 

        number_of_coins += 1 

    elif sum >= 0.1:
        sum -= 0.1
        sum=round(sum,2) 

        number_of_coins += 1

    elif sum >= 0.05:
        sum -= 0.05
        sum=round(sum,2) 
        
        number_of_coins += 1

    elif sum >= 0.02:
        sum -= 0.02
        sum=round(sum,2) 

        number_of_coins += 1

    elif sum >= 0.01:
        sum -= 0.01
        sum=round(sum,2) 

        number_of_coins += 1

        break

print(number_of_coins)



