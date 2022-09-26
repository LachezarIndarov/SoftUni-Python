"""
input1
8, 12, 38, 3, 17, 19, 25, 35, 50

output1
Group of 10's: [8, 3]
Group of 20's: [12, 17, 19]
Group of 30's: [25]
Group of 40's: [38, 35]
Group of 50's: [50]


input2
1, 3, 3, 4, 34, 35, 25, 21, 33

output2
Group of 10's: [1, 3, 3, 4]
Group of 20's: []
Group of 30's: [25, 21]
Group of 40's: [34, 35, 33]

"""

input_numbers = input().split(", ")
integer_list = list(map(int,input_numbers))
max_elem = max(integer_list)
filtered=list()

if max_elem % 2 > 0:
    upper_limit = int((max_elem//10)+1)
else:
    upper_limit = int(max_elem/10)

for i in range(10, (upper_limit*10)+10, 10):
    filtered.clear()
    after_removing = integer_list
    for x in range(0, len(after_removing)):
        if integer_list[x] <= i:
            filtered.append(integer_list[x])
            integer_list[x] = 0
    while 0 in integer_list:
        integer_list.remove(0)
    print(f"Group of {i}'s: {filtered}")
