"""
input1
2 4 6

output1
The minimum number is 2
The maximum number is 6
The sum number is: 12

input2
12 52 11 53 2 8 45

output2
The minimum number is 2
The maximum number is 53
The sum number is: 183

"""
def min_max_sum_func(nums):
    print(f' The minimum number is {min(nums)}')
    print(f' The maximum number is {max(nums)}')
    print(f' The sum number is: {sum(nums)}')


numbers = list(map(int,input().split(' ')))
min_max_sum_func(numbers)
