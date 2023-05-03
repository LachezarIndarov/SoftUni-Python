# readline - read only 3 chars from print text - print(file.readline(3))       Lachezar -> Lac
print(' --- line by line ---')
file = open('C:/Users/indarov/PycharmProjects/Exercise 1/Python Advanced/Lab/15.File Handling/Training/demo', 'r')

while True:
    line = file.readline()
    if not line:
        break
    print(line)

print(' --- line by line with chars count ---')
file = open('C:/Users/indarov/PycharmProjects/Exercise 1/Python Advanced/Lab/15.File Handling/Training/demo', 'r')

# while True:
#     line = file.readline(3)
#     if not line:
#         break
#     print(line)

print(file.readline(3))
print(file.readline(3))
print(file.readline(3))

print(' --- all lines ---')
file = open('C:/Users/indarov/PycharmProjects/Exercise 1/Python Advanced/Lab/15.File Handling/Training/demo', 'r')
print(file.readlines())
print(file.readlines())

print(' --- line by line with loop ---')
file = open('C:/Users/indarov/PycharmProjects/Exercise 1/Python Advanced/Lab/15.File Handling/Training/demo', 'r')
for line in file:
    print(line)

print(' --- line by line with comprehension ---')
file = open('C:/Users/indarov/PycharmProjects/Exercise 1/Python Advanced/Lab/15.File Handling/Training/demo', 'r')

print([
    line.strip() for line in file
])


# readline - read only 3 chars from print text - print(file.readline(3))       Lachezar -> Lac