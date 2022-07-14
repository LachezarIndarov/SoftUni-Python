"""
input1
2
2
sea
mountain
sea
sea
mountain

output1
Good job! Everything is sold.
Profit: 2358 leva.

input2
6
3
sea
mountain
mountain
mountain
sea
Stop

output2
Profit: 2857 leva.

"""

number_of_sea_excursions = int(input())
number_of_excursions_mountain = int(input())

packet_sea = number_of_sea_excursions
packet_mountain = number_of_excursions_mountain

sea = 680
mountain = 499
full_price = 0

command = input()

while command != "Stop":


    if command == "sea":
        if packet_sea == 0:
            full_price += 0
        else:
            full_price += sea
            packet_sea -= 1
    if command == "mountain":
        if packet_mountain == 0:
            full_price += 0
        else:
            full_price += mountain
            packet_mountain -= 1
    if packet_mountain == 0 and packet_sea == 0:
        print(f"Good job! Everything is sold.")
        break


    command = input()

print(f"Profit: {full_price} leva.")




