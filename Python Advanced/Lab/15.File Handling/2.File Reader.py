file = open('C:/Users/indarov/PycharmProjects/Exercise 1/Python Advanced/Lab/15.File Handling/Training/numbers.txt.', 'r')
the_sum = 0

for line in file:
    the_sum += int(line)

print(the_sum)
