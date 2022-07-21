"""
input1
5
10
3
2
-15
-4

output1
[10, 3, 2]
[-15, -4]
Count of positives: 3
Sum of negatives: -19

input2
6
11
2
35
599
31
20

output2
[11, 2, 35, 599, 31, 20]
[]
Count of positives: 6
Sum of negatives: 0

"""
number = int(input())

negatives = list()
positives = list()

sum_of_negatives = 0

for i in range(number):
    current = int(input())
    if current >= 0:
        positives.append(current)
    else:
        negatives.append(current)
        sum_of_negatives += current

print(positives)
print(negatives)

print(f"Count of positives: {len(positives)}")
print(f"Sum of negatives: {sum_of_negatives}")