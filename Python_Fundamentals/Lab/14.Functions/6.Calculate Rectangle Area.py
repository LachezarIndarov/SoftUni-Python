"""
input1
3
4

output1
12

input2
6
2

output2
12

"""

def calculate_rectangle_area(width,height):
    return width * height


current_width = int(input())
current_height = int(input())

print(calculate_rectangle_area(current_width,current_height))