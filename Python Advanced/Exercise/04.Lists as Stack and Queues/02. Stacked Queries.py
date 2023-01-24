"""
input1
9
1 97
2
1 20
2
1 26
1 20
3
1 91
4

output1
26
20
91, 20, 26


input2
10
2
1 47
1 66
1 32
4
3
1 25
1 16
1 8
4

output2
32
66
8
8, 16, 25, 32, 66, 47

"""
#GitHub  - 100% Judge

stack = []

queries_count = int(input())

for i in range(queries_count):
    queries_parts = [int(x) for x in input().split()]
    command = queries_parts[0]

    if command == 1:
        number = queries_parts[1]
        stack.append(number)

    # Check do you have elements in our "stack" list
    elif command == 2 and stack:
         stack.pop()

    # Check do you have elements in our "stack" list
    elif command == 3 and stack:
        # print element with maximum value in our stack
        print(max(stack))

    # Check do you have elements in our "stack" list
    elif command == 4 and stack:
        # print element with minimum value in our stack
        print(min(stack))


# After you go through all the queries, print the stack from top to bottom in the following format: 91,20,26
reversed_stack = []
while stack:
    reversed_stack.append(str(stack.pop()))

print(', '.join(reversed_stack))


