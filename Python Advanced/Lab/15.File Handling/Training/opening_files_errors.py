try:
    open('./demo2.txt') # This file exist
    print('File is found')
except FileNotFoundError:
    print('File is not found')


#---------------------------------------------
try:
    open('./demo3.txt') # This file don't exist
    print('File is found')
except FileNotFoundError:
    print('File is not found')

#----------------------------------------------
try:
    open('./nested_dir/demo2.txt') # File is not found - Here we have wrong directory
    print('File is found')
except FileNotFoundError:
    print('File is not found')


#----------------------------------------------
except FileNotFoundError:
    print('File is not found')
except IsADirectoryError:
    print('File is a directory')
except PermissionError:
    print('No permission to open file')