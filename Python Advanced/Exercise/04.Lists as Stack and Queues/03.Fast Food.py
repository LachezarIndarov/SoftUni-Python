"""
input1
348
20 54 30 16 7 9

output1
54
Orders complete

input2
499
57 45 62 70 33 90 88 76 100 50

output2
100
Orders left: 76 100 50

"""
#GitHub  - 100% Judge

from collections import deque

food_quantity = int(input())
orders = deque([int(x) for x in input().split()])

orders_are_complete = True

print(max(orders))

while orders:
      current_order = orders[0]

      if food_quantity >= current_order:
            food_quantity -= current_order
            orders.popleft()

      else:
            orders_are_complete = False
            break

if orders_are_complete :
    print("Orders complete")
else:
    str_orders = [str(x) for x in orders]
    print(f"Orders left: {' '.join(str_orders)}")

