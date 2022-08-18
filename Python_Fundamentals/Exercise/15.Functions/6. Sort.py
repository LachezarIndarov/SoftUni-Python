"""
input1
6 2 4

output1
[2, 4, 6]

input2
12 52 11 53 2 8 45

output2
[2, 8, 11, 12, 45, 52, 53]

"""
def sort_func(nums):
    return sorted(nums)


numbers = list(map(int,input().split(' ')))
print(sort_func((numbers)))