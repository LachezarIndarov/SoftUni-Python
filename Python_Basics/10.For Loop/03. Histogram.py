"""
input1
3
1
2
999

output1
66.67%
0.00%
0.00%
0.00%
33.33%

input2
4
53
7
56
999

output2
75.00%
0.00%
0.00%
0.00%
25.00%

input3
7
800
801
250
199
399
599
799

output3
14.29%
28.57%
14.29%
14.29%
28.57%

input4
9
367
99
200
799
999
333
555
111
9

output4
33.33%
33.33%
11.11%
11.11%
11.11%

"""

#!!!! #GitHub  - 100% Judge
n = int(input())
i = 0


p1 = 0
p2 = 0
p3 = 0
p4 = 0
p5 = 0

for i in range(0,n):
    num = int(input())

    if num < 200:
        p1 += 1

    elif num < 400:
        p2 += 1

    elif num < 600:
        p3 += 1

    elif  num < 800:
        p4 += 1

    else:
        p5 += 1

p1 = (p1 / n) * 100
p2 = (p2 / n) * 100
p3 = (p3 / n) * 100
p4 = (p4 / n) * 100
p5 = (p5 / n) * 100


print(f"{p1:.2f}%")
print(f"{p2:.2f}%")
print(f"{p3:.2f}%")
print(f"{p4:.2f}%")
print(f"{p5:.2f}%")





