# 'w' - create file or overwrite file
import time
from os import linesep

# linesep -> '\n' for Unix/Linux, '\n\r' for Windows

file = open('C:/Users/indarov/PycharmProjects/Exercise 1/Python Advanced/Lab/15.File Handling/Training/w_demos.txt', 'w')
file.write('--- w ---')
file.write(linesep)
file.write('It works!')
file.write(linesep)
file.write(str(time.time()))
file.write(linesep)

# 'a' - create file or append to file

file = open('C:/Users/indarov/PycharmProjects/Exercise 1/Python Advanced/Lab/15.File Handling/Training/a_demos.txt', 'a')
file.write('--- a ---')
file.write(linesep)
file.write('It works!')
file.write(linesep)
file.write(str(time.time()))
file.write(linesep)

# 'x' - create a new file or raise exception
file = open('C:/Users/indarov/PycharmProjects/Exercise 1/Python Advanced/Lab/15.File Handling/Training/x_demos.txt', 'x')
# file.write('--- x ---')
# file.write(linesep)
# file.write('It works!')
# file.write(linesep)
# file.write(str(time.time()))
# file.write(linesep)
