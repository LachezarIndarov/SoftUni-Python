"""
input1

George
Peter
William
Paid
Michael
Oscar
Olivia
Linda
End

output1
George
Peter
William

4 people remaining.

input2

Anna
Emma
Alexander
End

output2
3 people remaining.

"""
#GitHub  - 100% Judge

from collections import deque

queue = deque()

while True:
    command = input()

    if command == "End":
        print(f'{len(queue)} people remaining.')
        break

    elif command == "Paid":
        while queue:
            print(queue.popleft())
    else:
        queue.append(command)