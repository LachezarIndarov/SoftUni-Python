file_path = '/Users/indarov/PycharmProjects/Exercise 1/Python Advanced/Lab/15.File Handling/Training/demo'
#print_contents('/Users/indarov/PycharmProjects/Exercise 1/Python Advanced/Lab/15.File Handling/Training/demo')

print('--- Whole file ---')
file = open(file_path, 'r')
print(file.read())

print('--- by bytes count')
file = open(file_path, 'r')
while True:
    print(file.read(3))
#print(file.read(3))
#print(file.read(2))
#print(file.read(3))
#print(file.read(3))
#s = file.read(3)
#print(s)

#-------------------------------------------------------------------

file_path = '/Users/indarov/PycharmProjects/Exercise 1/Python Advanced/Lab/15.File Handling/Training/demo'
#print_contents('/Users/indarov/PycharmProjects/Exercise 1/Python Advanced/Lab/15.File Handling/Training/demo')

print('--- Whole file ---')
file = open(file_path, 'r')
print(file.read())

print('--- by bytes count')
file = open(file_path, 'r')
while True:
    print(file.read(3))
    if not chars:
        break
    print(chars)