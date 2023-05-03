for i in range(16):
    text = ''
    with open('C:/Users/indarov/PycharmProjects/Exercise 1/Python Advanced/Lab/15.File Handling/Training/demo-big.txt', 'r') as file:
        text = file.read()

    with open('C:/Users/indarov/PycharmProjects/Exercise 1/Python Advanced/Lab/15.File Handling/Training/demo-big.txt', 'a') as file:
        file.write(text)