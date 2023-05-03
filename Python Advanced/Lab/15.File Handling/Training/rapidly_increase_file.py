for _ in range(16):
    text = ''
    with open('C:/Users/indarov/PycharmProjects/Exercise 1/Python Advanced/Lab/15.File Handling/Training/demo-big.txt', 'r') as file_in:
        with open('C:/Users/indarov/PycharmProjects/Exercise 1/Python Advanced/Lab/15.File Handling/Training/demo-big.txt', 'a') as file_out:
            for line in file_in:
                file_out.write(line)

# Increases size by 2^n
'''
contents:
"
line 1
"
# Step 1

text = "
line 1
"

contents:
"
line 1
line 1
"
# Step 2

text = "
line 1
line 1
"
contents:
"
line 1
line 1
line 1
line 1
"
'''
