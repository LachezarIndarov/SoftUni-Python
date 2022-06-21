"""
input1
7

output1
1
2 3
4 5 6
7

input2
10

output2
1
2 3
4 5 6
7 8 9 10

input3
12

output3
1
2 3
4 5 6
7 8 9 10
11 12

input4
15

output4
1
2 3
4 5 6
7 8 9 10
11 12 13 14 15

"""
n = int(input())
current = 1
is_current_bigger_than_n = False

for row in range(1, n + 1):
    for col in range (1, row + 1):


        if current > n:
            is_current_bigger_than_n = True
            break
        print(str(current) + ' ', end='')
        current += 1
    if is_current_bigger_than_n:
        break
    print()
