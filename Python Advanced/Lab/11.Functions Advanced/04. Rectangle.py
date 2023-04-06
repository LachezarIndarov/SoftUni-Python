"""
Test Code1:
print(rectangle(2, 10))

output1
Rectangle area: 20
Rectangle perimeter: 24

Test Code2:
print(rectangle('2', 10))

output2
"Enter valid values!"

"""

def rectangle(length, width):
    def area():
        return length * width

    def perimeter():
        return 2 * (length + width)

    if not isinstance(length, int) \
            or not isinstance(width, int):
        return 'Enter valid values!'

    return f'''Rectangle area: {area()}
Rectangle perimeter: {perimeter()}'''


print(rectangle(2, 10))
print(rectangle('2', 10))
