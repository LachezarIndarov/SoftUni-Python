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

days_to_stay = int(input())
type_of_room = input()
assessment = input()


room_for_one_person = 18
apartment = 25
president_apartment = 35


number_of_nights = days_to_stay - 1
allfullprice = 0

if type_of_room == "room for one person":
    cost_of_stay = number_of_nights * room_for_one_person

elif type_of_room == "apartment":
    cost_of_stay = number_of_nights * apartment
    
    if days_to_stay < 10:
        cost_of_stay -= cost_of_stay * 0.3
    elif 10 <= days_to_stay <= 15:
        cost_of_stay -= cost_of_stay * 0.35
    elif days_to_stay > 15:
        cost_of_stay -= cost_of_stay * 0.5


elif type_of_room == "president apartment":
        cost_of_stay = number_of_nights * president_apartment
        
        if days_to_stay < 10:
            cost_of_stay -= cost_of_stay * 0.1
        elif 10 <= days_to_stay <= 15:
            cost_of_stay -= cost_of_stay * 0.15
        elif days_to_stay > 15:
            cost_of_stay -=  cost_of_stay * 0.2


if assessment == "positive":
    allfullprice = cost_of_stay + (cost_of_stay  * 0.25)
else:
    assessment == "negative"
    allfullprice = cost_of_stay  - (cost_of_stay * 0.1)


print(f"{allfullprice:.2f}")

