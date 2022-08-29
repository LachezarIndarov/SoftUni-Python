"""
input1
23
6
10

output1
19

input2
1
17
30

output2
-12

input3
42
58
100

output3
0

"""
a = int(input())
b = int(input())
c = int(input())

def sum_numbers():
    return a + b

def substract():
   return sum_numbers() - c


print(substract())
