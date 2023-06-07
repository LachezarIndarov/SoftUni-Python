"""
input1
10 16 13 25
12 11 8

output1
Toys: 3
Energy: 31
Elves left: 3, 6, 26, 14

comments 1:
1) The elf with energy 10 takes the box with 8 materials. He creates 1 gift and uses 8 units of energy. He eats a cookie and goes to the end of the line, which now looks like this: 16 13 25 3.
2) The elf with energy 16 takes the box with 11 materials. He creates 1 gift and uses 11 units of energy. Then, he eats a cookie and goes to the end of the line, which now looks like this: 13 25 3 6.
3) The elf with energy 13 takes the box with 12 materials. It is the third time an elf takes a box. The elf does not have the needed energy: 12 * 2, so he drinks a hot chocolate and goes to the end of the line: 25 3 6 26.
4) The elf with energy 25 takes the box with 12 materials. It is the fourth time an elf takes a box. He creates 1 gift and uses 12 units of energy. He eats a cookie and goes to the end of the line, which now looks like this: 3 6 26 14.
No boxes are left, so the program ends. Print the desired text.

input2
10 14 22 4 5
11 16 17 11 1 8

output2
Toys: 7
Energy: 75
Elves left: 10, 14

input3
5 6 7
2 1 5 7 5 3

output3
Toys: 3
Energy: 20
Boxes left: 2, 1

"""

from collections import deque

elf_energies = deque([int(x) for x in input().split(' ')])
boxes = [int(x) for x in input().split(' ')]

turns_count = 0
total_energy_spend = 0
toys_count = 0

while boxes and elf_energies:

    while elf_energies and elf_energies[0] < 5:
        elf_energies.popleft()

    if not elf_energies:
        break

    box = boxes.pop()
    elf_energy = elf_energies.popleft()

    turns_count += 1

    toys_to_be_created_count = 1
    energy_to_be_spend = box
    energy_increase_factory = 1

    if turns_count % 3 == 0:
        toys_to_be_created_count = 2
        energy_to_be_spend *= 2
    if turns_count % 5 == 0:
        toys_to_be_created_count = 0
        energy_increase_factory = 0

    if energy_to_be_spend <= elf_energy:
        toys_count += toys_to_be_created_count
        total_energy_spend += energy_to_be_spend
        elf_energies.append(elf_energy - energy_to_be_spend + energy_increase_factory)

    else:
        boxes.append(box)
        elf_energies.append(elf_energy * 2)


print(f'Toys: {toys_count}')
print(f'Energy: {total_energy_spend}')
if elf_energies:
    elves_string = ', '.join(str(x) for x in elf_energies)
    print(f'Elves left: {elves_string}')
if boxes:
    boxes_string = ', '.join(str(x) for x in boxes)
    print(f'Boxes left: {boxes_string}')



