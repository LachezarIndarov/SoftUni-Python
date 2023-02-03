"""
input1
8
Lee
Joey
Lee
Joe
Alan
Alan
Peter
Joey

output1
Alan
Joey
Lee
Joe
Peter

input2
7
Lyle
Bruce
Alice
Easton
Shawn
Alice
Shawn

output2
Easton
Lyle
Alice
Bruce
Shawn

"""

# Variant 2
# n = int(input())
#
# names_set = set()  # not {}
#
# for _ in range(n):
#     names_set.add(input())
#
# # [print(name) for name in names_set]
# for name in names_set:
#     print(name)
#

n = int(input())
names_set = {input() for _ in range(n)}
[print(name) for name in names_set]

# Don't do this
# [print(name) for name in {input() for _ in range(int(input()))}]
