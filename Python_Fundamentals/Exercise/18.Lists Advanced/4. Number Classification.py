"""
input1
1, -2, 0, 5, 3, 4, -100, -20, 12, 19, -33

output1
Positive: 1, 0, 5, 3, 4, 12, 19
Negative: -2, -100, -20, -33
Even: -2, 0, 4, -100, -20, 12
Odd: 1, 5, 3, 19, -33


input2
1, 2, 53, 2, 21

output2
Positive: 1, 2, 53, 2, 21
Negative:
Even: 2, 2
Odd: 1, 53, 21


"""

numbers = list(map(int, input().split(', ')))

positive =[str(x) for x in numbers  if x >= 0]
negative = [str(x) for x in numbers  if x < 0]
even = [str(x) for x in numbers  if x % 2 == 0]
Odd = [str(x) for x in numbers  if x % 2 != 0]

print(f"Positive: {', '.join(positive)}")
print(f"Negative: {', '.join(negative)}")
print(f"Even: {', '.join(even)}")
print(f"Odd: {', '.join(Odd)}")





