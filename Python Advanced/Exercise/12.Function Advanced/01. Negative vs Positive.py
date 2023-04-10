"""
input1
1 2 -3 -4 65 -98 12 57 -84

output1
-189
137
The negatives are stronger than the positives


input2
1 2 3

output2
0
6
The positives are stronger than the negatives
"""

def find_positive_and_negative_sums(*args):
    positive_sum = 0
    negative_sum = 0

    for i in args:
        if i > 0:
            positive_sum += i
        else:
            negative_sum += i
    return positive_sum, negative_sum

nums = [int(x) for x in input().split()]

positive_sum, negative_sum = find_positive_and_negative_sums(*nums)
print(negative_sum)
print(positive_sum)

if abs(negative_sum) > positive_sum:
     print("The negatives are stronger than the positives")

else:
     print("The positives are stronger than the negatives")
