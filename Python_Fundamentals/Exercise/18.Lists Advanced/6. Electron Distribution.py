"""
input1
10

output1
[2, 8]

input2
44

output2
[2, 8, 18, 16]

"""

def electron_distribution(number):
    filled_shells = []
    counter = 1
    while True:
        element = 2 * (counter ** 2)

        if element < number:
            number -= element
            filled_shells.append(element)
        else:
            filled_shells.append(number)
            break
        counter += 1

    print(filled_shells)

data = int(input())
electron_distribution(data)