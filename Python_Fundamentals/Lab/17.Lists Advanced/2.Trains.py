"""
input1
3
add 20
insert 0 15
leave 0 5
End

output1
[10, 0, 20]

input2
5
add 10
add 20
insert 0 16
insert 1 44
leave 1 12
insert 2 100
insert 4 61
leave 4 1
add 15
End

output2
[16, 32, 100, 0, 105]
"""

num_wagons = int(input())

train = [0 for i in range(num_wagons)]
command = input()

while command != "End":
    explode = command.split(" ")
    current = explode[0]

    if current == "add":
        num_people = int(explode[1])
        train[-1] += num_people

    if current == "insert":
        position = int(explode[1])
        num_people = int(explode[2])
        train[position] += num_people

    if current == "leave":
        position = int(explode[1])
        num_people = int(explode[2])
        train[position] -= num_people

    command = input()

print(train)



