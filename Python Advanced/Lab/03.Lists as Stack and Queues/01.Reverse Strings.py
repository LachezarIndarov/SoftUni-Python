"""
input1
I Love Python

output1
nohtyP evoL I

input2
Stacks and Queues

output2
seueuQ dna skcatS
"""
#GitHub  - 100% Judge

original_string = input()

# Better solutions
# original_string[::-1]
# original_string.reverse()

# Check how it's work "stack".
stack = []

for i in original_string:
    # push into the stack
    stack.append(i)

reversed_string = ""

while stack:
    # pop the top element
    reversed_string += stack.pop()

print(reversed_string)
