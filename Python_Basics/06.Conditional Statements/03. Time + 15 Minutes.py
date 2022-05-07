"""
input1
1
46

output1
2:01

input2
0
01

output2
0:16

input3
23
59

output3
0:14
"""

hours = int(input())
minutes = int(input())

minutes += 15

if minutes >= 60:
    hours += 1
    minutes %= 60


if  hours > 23:
    hours = 0




if minutes <= 9:
    print(f'{hours}:0{minutes}')
else:
    print(f'{hours}:{minutes}')








