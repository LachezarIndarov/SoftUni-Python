"""
input1
1.2.3

output1
1.2.4

input2
1.3.9

output2
1.4.0

input3
3.9.9

output3
4.0.0

"""
def next_version(version_number):
    version_number = int(''.join(data)) + 1
    result = [str(num) for num in str(version_number)]
    print('.'.join(result))


data = input().split('.')
next_version(data)


