"""
input1
123, 323, 421, 121

output1
False
True
False
True

input2
32, 2, 232, 1010

output2
False
True
True
False

"""

def palindrome_integers(nums):

  for num in nums:

    if  num == num[::-1]:
        print("True")
    else:
        print("False")


numbers = input().split(', ')
palindrome_integers(numbers)