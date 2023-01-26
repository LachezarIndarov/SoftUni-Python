"""
input1
5 4 8 6 3 8 7 7 9
16

output1
5

input2
1 7 8 2 5 4 7 8 9 6 3 2 5 4 6
20

output2
5
"""
#GitHub  - 100% Judge

clothes = [int(x) for x in input().split()]
rack_capacity = int(input())

current_rack_capacity = rack_capacity
racks_counter = 1

while clothes:
    piece_of_clothing = clothes[-1]

    if piece_of_clothing > current_rack_capacity:
        racks_counter += 1
        current_rack_capacity = rack_capacity

    else:
        current_rack_capacity -= piece_of_clothing
        clothes.pop()

print(racks_counter)