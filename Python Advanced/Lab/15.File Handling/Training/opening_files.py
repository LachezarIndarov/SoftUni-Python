from io import open

#import io
def print_contents(file_path):
    file = open(file_path)
    print(file.read())

# Relative
print_contents('./demo2.txt')
print_contents('./opening_files.py')
print_contents('/Users/indarov/PycharmProjects/Exercise 1/Python Advanced/Lab/15.File Handling/Training/demo')
print_contents('C:/Users/indarov/PycharmProjects/Exercise 1/Python Advanced/Lab/15.File Handling/Training/demo')




