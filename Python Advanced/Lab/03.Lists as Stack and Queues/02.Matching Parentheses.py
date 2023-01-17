"""
input1
1 + (2 - (2 + 3) * 4 / (3 + 1)) * 5

output1
(2 + 3)
(3 + 1)
(2 - (2 + 3) * 4 / (3 + 1))

input2
(2 + 3) - (2 + 3)

output2
(2 + 3)
(2 + 3)

"""
#GitHub  - 100% Judge

expression = input()

stack = []
for i in range(len(expression)):
    ch = expression[i]
    if ch == '(':
        stack.append(i)
    elif ch == ')':
        start_index = stack.pop()
        end_index = i + 1
        print(expression[start_index:end_index])

