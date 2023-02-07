"""
input1
5
7IK9Yo0h
9NoBUajQ
Ce8vwPmE
SVQXQCbc
tSzE5t0p
9NoBUajQ
Ce8vwPmE
SVQXQCbc
END

output1
2
7IK9Yo0h
tSzE5t0

input2
6
m8rfQBvl
fc1oZCE0
UgffRkOn
7ugX7bm0
9CQBGUeJ
2FQZT3uC
2FQZT3uC
9CQBGUeJ
fc1oZCE0
END

output2
3
7ugX7bm0
UgffRkOn
m8rfQBvl
"""

def is_vip(guest):
    return guest[0].isdigit()


n = int(input())

vip_guests = set()
regular_guests = set()

for _ in range(n):
    reservation = input()
    if is_vip(reservation):
        vip_guests.add(reservation)
    else:
        regular_guests.add(reservation)

while True:
    guest = input()
    if guest == 'END':
        break

    if is_vip(guest):
        vip_guests.remove(guest)
    else:
        regular_guests.remove(guest)

print(len(vip_guests) + len(regular_guests))
[print(guest) for guest in sorted(vip_guests)]
[print(guest) for guest in sorted(regular_guests)]

