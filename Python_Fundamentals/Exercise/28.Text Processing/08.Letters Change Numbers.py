""""
Input 1                                      Output1
A12b s17G	                                 330.00

Comments: 12/1=12, 12+2=14, 17*19=323, 323–7=316, 14+316=330

Input 2                                     Output2
P34562Z q2576f   H456z	                    46015.12

Input 3                                     Output 3
a1A	                                        0.00



"""

from string import ascii_lowercase


def extract_func(text):
    current_num = [num for num in text if num.isdigit()]
    result = 0

    for i in range(len(text)):
        if text[i].isalpha():
            index = ascii_lowercase.index(text[i].lower()) + 1

            if i == 0:
                if text[i] == text[i].lower():
                    result = int(''.join(current_num)) * index
                else:
                    result = int(''.join(current_num)) / index
            else:
                if text[i] == text[i].lower():
                    result += index
                else:
                    result -= index
    return result


def letters_change_numbers(data):
    result = 0

    for num in data:
        result += extract_func(num)

    print(f'{result:.2f}')

data = input().split()
letters_change_numbers(data)

