from os import remove
from os.path import exists

file_path = 'C:/Users/indarov/PycharmProjects/Exercise 1/Python Advanced/Lab/15.File Handling/Training/to_delete.txt'

# open(file_path, 'w').close()
if exists(file_path):
    remove(file_path)
    print('File deleted')
else:
    print('File already deleted')