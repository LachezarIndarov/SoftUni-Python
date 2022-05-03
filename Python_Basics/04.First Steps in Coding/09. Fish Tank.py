"""
input1
85
75
47
17

output1
248.68875


input2
105
77
89
18.5

output2
586.445475

"""
#GitHub  - 100% Judge

length_of_the_aquarium = int(input())
width_of_the_aquarium = int(input())
height_of_the_aquarium = int(input())
percentage = float(input())

volume_of_the_aquarium = length_of_the_aquarium * width_of_the_aquarium * height_of_the_aquarium
volume_of_liters = volume_of_the_aquarium / 1000
occupied_space = percentage / 100

required_liters = volume_of_liters * (1 - occupied_space)

print(required_liters)