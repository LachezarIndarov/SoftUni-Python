"""
input1
100000
100050

output1
100001 100012 100023 100034 100045

input2
123456
124000

output2
123464 123475 123486 123497 123530 123541 123552 123563 123574 123585 123596 123640 123651 123662 123673 123684 123695 123750 123761 123772 123783 123794 123860 123871 123882 123893 123970 123981 123992

input3
299900
300000

output3
299970 299981 299992

"""

first_num = int(input())
second_num = int(input())

for number in range(first_num,second_num + 1):
    number_to_str = str(number)
    even_sum = 0
    odd_sum = 0

    for index, digit in enumerate(number_to_str):
        if index % 2 == 0:
            even_sum += int(digit)
        else:
            odd_sum += int(digit)

    if even_sum == odd_sum:
        print(number, end=' ')

