"""
Test Code1:
print(fill_the_box(2, 8, 2, 2, 1, 7, 3, 1, 5, "Finish"))

output1
There is free space in the box. You could put 13 more cubes.

Comment:
The size of the box: 2 * 8 * 2 = 32
We put the cubes consistently. At the end there is more free space left.


Test Code2:
print(fill_the_box(5, 5, 2, 40, 11, 7, 3, 1, 5, "Finish"))

output2
No more free space! You have 17 more cubes.

Comment:
The size of the box: 5 * 5 * 2 = 50
We put the cubes consistently. First, we put 40 cubes and there is free space left. Then we try to put 11 cubes, but there is only space for 10.
Cubes left: 1 + 7 + 3 + 1 + 5 = 17


Test Code3:
print(fill_the_box(10, 10, 10, 40, "Finish", 2, 15, 30))

output3
There is free space in the box. You could put 960 more cubes.

"""

def fill_the_box(height, length, width, *args):
    volume = height * length * width
    left_cubes = 0

    for el in args:
        if el == 'Finish':
            break

        if volume >= el:
            volume -= el
        else:
            el -= volume
            left_cubes += el
            volume = 0

    if volume:
        return f'There is free space in the box. You could put {volume} more cubes.'
    else:
        return f'No more free space! You have {left_cubes} more cubes.'

print(fill_the_box(2, 8, 2, 2, 1, 7, 3, 1, 5, "Finish"))
print(fill_the_box(5, 5, 2, 40, 11, 7, 3, 1, 5, "Finish"))
print(fill_the_box(10, 10, 10, 40, "Finish", 2, 15, 30))