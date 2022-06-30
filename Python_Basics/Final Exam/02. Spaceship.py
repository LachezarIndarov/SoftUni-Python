"""
input1
3.5
4
5
1.70

output1
The spacecraft holds 8 astronauts.

input2
4.5
4.8
5
1.75

output2
The spacecraft is too big.

input3
3
3
4
1.68

output3
The spacecraft holds 4 astronauts.

"""

import math

ship_width = float(input())
length_of_ship = float(input())
ship_height = float(input())
average_height_of_astronaut = float(input())

rocket_volume = ship_width * length_of_ship * ship_height
room_volume = (average_height_of_astronaut + 0.4)*2*2
number_of_astronauts = rocket_volume / room_volume

if number_of_astronauts < 3:
    print(f"The spacecraft is too small.")
elif 3 <= number_of_astronauts <= 10:
    print(f"The spacecraft holds {math.floor(number_of_astronauts)} astronauts.")
else:
    print(f"The spacecraft is too big.")

