"""
Input1
sh, too_long_username, !lleg@l ch@rs, jeffbutt

Output1
jeffbutt

Input2
Jeff, john45, ab, cd, peter-ivanov, @smith

Output2
Jeff
John45
peter-ivanov


"""
import string

def valid_username(data):

    flag = 0
    expected_elements = string.digits + string.ascii_letters + "_" + "-"

    for name in data:
        flag = 0
        if 3 > len(name) or len(name) > 16:
            flag = 1


        elif len([x for x in name if x in expected_elements]) != len(name):
            flag = 1

        elif flag == 0:
            print(name)

d = input().split(', ')
valid_username(d)





