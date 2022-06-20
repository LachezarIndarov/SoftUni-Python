"""
input1
10
10
2
20
20
20
20
122

output1
No more free space! You need 2 Cubic meters more.

input2
10
1
2
4
6
Done

output2
10 Cubic meters left.

"""
width_of_free_space = int(input())
length_of_free_space = int(input())
height_of_free_space = int(input())

available_cubic_meters = width_of_free_space * length_of_free_space * height_of_free_space

while True:

    free_volume = input()
    if free_volume == "Done":
        print(f"{available_cubic_meters} Cubic meters left.")
        break


    available_cubic_meters -= int(free_volume)


    if available_cubic_meters <= 0:
        print(f"No more free space! You need {abs(available_cubic_meters)} Cubic meters more.")
        break


