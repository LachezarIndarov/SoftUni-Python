"""
input1
10
IN, CA2844AA
IN, CA1234TA
OUT, CA2844AA
IN, CA9999TT
IN, CA2866HI
OUT, CA1234TA
IN, CA2844AA
OUT, CA2866HI
IN, CA9876HH
IN, CA2822UU

output1
CA2844AA
CA9999TT
CA2822UU
CA9876HH

input2
4
IN, CA2844AA
IN, CA1234TA
OUT, CA2844AA
OUT, CA1234TA

output2
Parking Lot is Empty

"""
n = int(input())

parking_lot_logs = [input().split(', ') for _ in range(n)]

parking_lot = set()

for direction, car_number in parking_lot_logs:
    if direction == 'IN':
        parking_lot.add(car_number)
    elif car_number in parking_lot:
        parking_lot.remove(car_number)

if parking_lot:
    [print(car_number) for car_number in parking_lot]
else:
    print('Parking Lot is Empty')
