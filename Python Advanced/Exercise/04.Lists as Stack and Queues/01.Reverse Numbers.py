"""
input1
1 2 3 4 5
output1
5 4 3 2 1

input1
1
output1
1
"""
#GitHub  - 100% Judge

numbers = input().split()

while numbers:
    last_number = numbers.pop()
    print(last_number, end=" ")