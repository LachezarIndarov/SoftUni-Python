"""
input1
Tracy Emily Daniel
2

output1
Removed Emily
Removed Tracy
Last is Daniel

input2
George Peter Michael William Thomas
10

output2
Removed Thomas
Removed Peter
Removed Michael
Removed George
Last is William

input3
George Peter Michael William Thomas
1

output3
Removed George
Removed Peter
Removed Michael
Removed William
Last is Thomas

"""
"""
George Peter Michael William Thomas - Every 3 person left the game
3


George Peter Michael William Thomas
  1       2       3
George  Peter   William   Thomas
  3                1         2
Peter  William   Thomas
  1        2        3

Peter William
  1      2
  3
  
William - Winner  
"""
#GitHub  - 100% Judge

from collections import deque

kids_string = input()
tosses_count_string = input()

kids = deque(kids_string.split(" "))
tosses_count = int(tosses_count_string)

current_count = 0
while len(kids) > 1:
    current_count += 1

    kid = kids.popleft()

    if current_count < tosses_count:
        kids.append(kid)

    else:
        print(f"Removed {kid}")
        current_count = 0
print(f"Last is {kids.popleft()}")