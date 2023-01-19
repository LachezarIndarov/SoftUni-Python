"""
input1
2
Peter
Amy
Start
2
refill 1
1
End

output1
Peter got water
Amy got water

0 liters left

input2
10
Peter
George
Amy
Alice
Start
2
3
3
3
End

output2
Peter got water
George got water
Amy got water
Alice must wait

2 liters left


Comment:
We create a queue with Peter and Amy. After the start command,
we see that Peter wants 2 liters of water (and he gets them).
The water dispenser is left with 0 liters.
After refilling, there is 1 liter in the dispenser.
So when Amy wants 1 liter, she gets it, and there are 0 liters left in the dispenser.

"""
#GitHub  - 100% Judge
from collections import deque

water_quantity = int(input())
people = deque()

while True:
    command = input()
    if command == "Start":
        break

    people.append(command)

while True:
    command = input()
    if command == "End":
        break

    elif command.startswith("refill"):
        params = command.split(" ")
        water_quantity += int(params[1])

    else:
        person = people.popleft()
        water_wanted = int(command)

        if water_wanted <= water_quantity:
            print(f"{person} got water")
            water_quantity -= water_wanted
        else:
            print(f"{person} must wait")

print(f"{water_quantity} liters left")