# Stack - стекове

stack = []

stack.append(1)
stack.append(2)
stack.append(3)
stack.append(4)
stack.append(5)
stack.append(6)
stack.append(7)
stack.append(8)
stack.append(9)

print(stack) # [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Peek - print
print(stack[-1]) # 9 - Последния елемент от списъка "stack[-1]"
print(stack)     # [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Pop - remove
stack.pop()  # [1, 2, 3, 4, 5, 6, 7, 8]
print(stack) # [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Push - add,append
stack.append(9)
print(stack)

# not stack operation - Това са операции на списъците но не са операции на стековете
stack.insert()
stack.reverse()
stack.sort()
stack.pop(0)