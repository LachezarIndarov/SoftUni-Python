"""
input1
20 62 99 35 0 150
120 60 10 1 70 10
+ - + + / * - - /

output1
Total honey made: 148
Bees left: 99, 35, 0, 150


input2
30
15 9 5 150 8
* + + * -

output2
Total honey made: 4500
Nectar left: 15, 9, 5

Comments:
First, compare 20 to 10. 20 is bigger than 10, so remove 10. Then compare 20 to 70. 20 is less than 70, so the bee could return to the hive. Honey made with given nectar is 20 + 70 = 90.
Next, compare 62 to 1. 62 is bigger than 1, so remove 1. Compare 62 to 10. 62 is bigger than 10, so remove 10. Compare 62 to 60. 62 is bigger than 60, so remove 60. Compare 62 to 120. 60 is less than 120, so the bee could return to the hive. Honey made with given nectar is 62 - 120 = (-58). (-58) is negative, and its absolute value is 58, so the calculation result is 58.
Total honey made: 90 + 58 = 148.
Print desired text.

"""

from collections import deque

bees = deque([int(x) for x in input().split()])
nectars = [int(x) for x in input().split()]
operators = deque(input().split())

honey = 0

operations  = {

    '+': lambda a, b: a + b,
    '-': lambda a, b: a - b,
    '*': lambda a, b: a * b,
    '/': lambda a, b: a / b
}

while bees and nectars:
    bee = bees.popleft()
    nectar = nectars.pop()

    if nectar < bee:
       bees.appendleft(bee)
       continue

    if nectar == 0:
        continue

    operator = operators.popleft()
    honey += abs(operations[operator](bee, nectar))

print(f'Total honey made: {honey}')

if bees:
    print(f'Bees left: {", ".join([str(x) for x in bees])}')

if nectars:
    print(f'Nectar left: {", ".join([str(x) for x in nectars])}')