"""
input1
6 3 - 2 1 * 5 /

output1
1

input2
2 2 - 1 *

output2
0

input3
10 23 * 4 2 / 30 10 + 100 50 - 2 -1 *

output3
164
"""
from collections import deque

expression = input().split()
nums = deque()

operations  = {

    '+': lambda a, b: a + b,
    '-': lambda a, b: a - b,
    '*': lambda a, b: a * b,
    '/': lambda a, b: a // b
}

for ch in expression:
    if ch in '+-/*':
        while len(nums) > 1:
            left = nums.popleft()
            right = nums.popleft()
            result = operations[ch](left, right)
            nums.appendleft(result)
    else:
        nums.append(int(ch))

print(nums.popleft())