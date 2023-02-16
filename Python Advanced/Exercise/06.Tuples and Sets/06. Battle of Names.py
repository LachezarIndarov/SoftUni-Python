"""
input1
4
Pesho
Stefan
Stamat
Gosho

output1
304, 128, 206, 511

input2
6
Preslav
Gosho
Ivan
Stamat
Pesho
Stefan

output2
733, 101

Comment:
First name: Pesho. The sum of the ASCII values is: 80 + 101 + 115 + 104 + 111 = 511. Integer divide the sum to the current row (1): 511 / 1 = 511.
Second name: Stefan. The sum of the ASCII values is: 83 + 116 + 101 + 102 + 97 + 110 = 609. Integer divide the sum to the current row (2): 609 / 2 = 304.
Third name: Stamat. The sum of the ASCII values is: 83 + 116 + 97 + 109 + 97 + 116 = 618. Integer divide the sum to the current row (3): 618 / 3 = 206.
Fourth name: Gosho. The sum of the ASCII values is: 71 + 111 + 115 + 104 + 111 = 512. Integer divide the sum to the current row (4): 512 / 4 = 128.
The odd set: 511
The even set: 304, 206, 128
The sum of the even numbers is larger, so we print the symmetric-different values.


"""

n = int(input())

even = set()
odd = set()

for row in range(1,n + 1):
    name = input()
    name_sum = sum([ord(x) for x in name]) // row
    if name_sum % 2 == 0:
        even.add(name_sum)
    else:
        odd.add(name_sum)

even_sum = sum(even)
odd_sum = sum(odd)

if even_sum == odd_sum:
    result = odd.union(even)

elif even_sum > odd_sum:
    result = odd.symmetric_difference(even)

else:
    result = odd.difference(even)

print(*result, sep=', ')
