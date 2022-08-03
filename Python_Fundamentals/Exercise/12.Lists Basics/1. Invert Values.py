"""
input1
1 2 -3 -3 5

output1
[-1, -2, 3, 3, -5]

input2
-4 0 2 57 -101

output2
[4, 0, -2, -57, 101]

"""

numbers = input().split(' ')

new_list =[]

for num in (numbers):
    if int(num) > 0:
        new_list.append(-int(num))

    else:
        new_list.append(abs(int(num)))

print(new_list)

