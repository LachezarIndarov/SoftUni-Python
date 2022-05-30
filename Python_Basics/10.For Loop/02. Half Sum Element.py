"""
input1
7
3
4
1
1
2
12
1


output1
Yes
Sum = 12

comments:
3 + 4 + 1 + 2 + 1 + 1 = 12

input2
4
6
1
2
3

output2
Yes
Sum = 6


input3
3
1
1
10

output3
No
Diff = 8

input4
3
5
5
1

output4
No
Diff = 1

input5
3
1
1
1

output5
No
Diff = 1

"""
#GitHub  - 100% Judge
import sys

max_num = -sys.maxsize
sum_numbers = 0

n = int(input())

for i in range(0, n):
    num = int(input())
    if num > max_num:
        max_num = num
    sum_numbers += num

if max_num == sum_numbers - max_num:
    print("Yes")
    print(f"Sum = {max_num}")

else:
    print("No")
    sum_others = sum_numbers - max_num
    print (f"Diff = {abs(max_num - sum_others)}")


