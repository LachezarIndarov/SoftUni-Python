"""
input1
3
0,3-1,2
2,10-3,5
6,15-3,10

output1
Longest intersection is [6, 7, 8, 9, 10] with length 5

input2
5
0,10-2,5
3,8-1,7
1,8-2,4
4,7-2,5
1,10-2,11

output2
Longest intersection is [2, 3, 4, 5, 6, 7, 8, 9, 10] with length 9

Comment:
The intersection of [0-3] and [1-2] is [1-2] (length 2)
The intersection of [2-10] and [3-5] is [3-5] (length 3)
The intersection of [6-15] and [3-10] is [6-10] (length 5) - which is the longest

"""

n = int(input())
best_intersection = set()

for i in range(n):
    first_range, second_range = input().split('-')

    first_start, first_end = [int(x) for x in first_range.split(',')]
    second_start, second_end = [int(x) for x in second_range.split(',')]

    first = set(range(first_start,first_end + 1))
    second = set(range(second_start,second_end + 1))

    current_intersection = first.intersection(second)
    if len(current_intersection) > len(best_intersection):
        best_intersection = current_intersection
print(f'Longest intersection is [{", ".join([str(x) for x in best_intersection])}] with length {len(best_intersection)}')