"""
input1
6
George
George
George
Peter
George
NiceGuy1234

output1
George
Peter
NiceGuy1234

input2
10
Peter
Maria
Peter
George
Steve
Maria
Alex
Peter
Steve
George

output2
Peter
Maria
George
Steve
Alex

"""

n = int(input())

usernames = set()
for i in range(n):
    username = input()
    usernames.add(username)

for username in usernames:
    print(username)