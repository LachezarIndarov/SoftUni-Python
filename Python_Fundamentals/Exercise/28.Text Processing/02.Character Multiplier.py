"""
Input1
George Peter

Output1
52114

Input2
123 522

Output2
7647

Input3
a aaaa

Output3
9700

"""


def sum_func(first_word, second_word):
    total_sum = 0

    for i in range(len(first_word)):
        if i < len(second_word):
            total_sum  += ord(first_word[i]) * ord(second_word[i])
        else:
            total_sum += ord(first_word[i])
    return total_sum

def char_multiplier(first_word, second_world):
    result = 0
    if len(first_word) > len(second_world):
        result = sum_func(first_word, second_world)
    else:
        result = sum_func(second_world, first_word)

    print(result)


data = input().split(' ')
char_multiplier(data[0],data[1])

