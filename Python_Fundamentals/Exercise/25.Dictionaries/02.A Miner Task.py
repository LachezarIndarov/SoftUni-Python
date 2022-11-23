"""
Input1
Gold
155
Silver
10
Copper
17
stop

output1
Gold -> 155
Silver -> 10
Copper -> 17

Input2
gold
155
silver
10
copper
17
gold
15
stop

Output2
gold -> 170
silver -> 10
copper -> 17

"""

def miner_task():


    item_dictionary = {}


    while True:
        resource = input()

        if resource == 'stop':
            break

        quantity = int(input())

        if resource not in item_dictionary:
            item_dictionary[resource] = quantity
        else:
            item_dictionary[resource] += quantity

    for key, value in item_dictionary.items():
        print(f"{key} -> {value}")

miner_task()





