"""
Input1
5
register John CS1234JS
register George JAVA123S
register Andy AB4142CD
register Jesica VR1223EE
unregister Andy

Output1
John registered CS1234JS successfully
George registered JAVA123S successfully
Andy registered AB4142CD successfully
Jesica registered VR1223EE successfully
Andy unregistered successfully
John => CS1234JS
George => JAVA123S
Jesica => VR1223EE

Input2
4
register Jony AA4132BB
register Jony AA4132BB
register Linda AA9999BB
unregister Jony

Output2
Jony registered AA4132BB successfully
ERROR: already registered with plate number AA4132BB
Linda registered AA9999BB successfully
Jony unregistered successfully
Linda => AA9999BB

Input3
6
register Jacob MM1111XX
register Anthony AB1111XX
unregister Jacob
register Joshua DD1111XX
unregister Lily
register Samantha AA9999BB

Output3
Jacob registered MM1111XX successfully
Anthony registered AB1111XX successfully
Jacob unregistered successfully
Joshua registered DD1111XX successfully
ERROR: user Lily not found
Samantha registered AA9999BB successfully
Anthony => AB1111XX
Joshua => DD1111XX
Samantha => AA9999BB




"""
number_of_commands = int(input())

registered_dict = {}

for command in range(number_of_commands):
    info = input().split(" ")

    if info[0] == "register":
        name = info[1]
        plate = info[2]

        if name not in registered_dict.keys():
            registered_dict[name] = plate
            print(f"{name} registered {plate} successfully")
        else:
            print(f"ERROR: already registered with plate number {plate}")

    elif info[0] == "unregister":
        name = info[1]
        if name not in registered_dict.keys():
            print(f"ERROR: user {name} not found")
        else:
            print(f"{name} unregistered successfully")
            registered_dict.pop(name)

[print(f"{name} => {plate}") for name, plate in registered_dict.items()]
