"""
input1
1000435

output1
Odd sum = 9, Even sum = 4

input2
3495892137259234

output2
Odd sum = 54, Even sum = 22

"""
def odd_even_sum(nums):
    odd_sum = 0
    even_sum = 0

    for num in nums:
        if num % 2 == 0:
            even_sum += num
        else:
            odd_sum += num



    print(f'Odd sum = {odd_sum}, Even sum = {even_sum}')

numbers = map(int, list(input()))

odd_even_sum(numbers)