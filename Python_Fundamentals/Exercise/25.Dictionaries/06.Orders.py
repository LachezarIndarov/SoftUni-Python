"""
Input1

Beer 2.20 100
IceTea 1.50 50
NukaCola 3.30 80
Water 1.00 500
buy

Output1

Beer -> 220.00
IceTea -> 75.00
NukaCola -> 264.00
Water -> 500.00

Input2
Beer 2.40 350
Water 1.25 200
IceTea 5.20 100
Beer 1.20 200
IceTea 0.50 120
buy

Output2
Beer -> 660.00
Water -> 250.00
IceTea -> 110.00

Input3
CesarSalad 10.20 25
SuperEnergy 0.80 400
Beer 1.35 350
IceCream 1.50 25
buy

Output3
CesarSalad -> 255.00
SuperEnergy -> 320.00
Beer -> 472.50
IceCream -> 37.50


"""

def orders_func(orders_dict,command):
    product = command[0]
    price = float(command[1])
    quantity = int(command[2])

    if product in orders_dict:
        orders_dict[product] = [price,(quantity + orders_dict[product][1])]

    else:
        orders_dict[product] = [price, quantity]

    return orders_dict

def orders():

    orders_dict = {}

    while True:
        command = input()

        if command == "buy":
            break

        command = command.split(' ')

        orders_dict = orders_func(orders_dict, command)


    for i in orders_dict:

        total_sum = orders_dict[i][0] * orders_dict[i][1]
        print(f"{i} -> {total_sum:.2f}")


orders()








