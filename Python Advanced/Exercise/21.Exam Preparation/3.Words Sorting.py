"""
Test Code1
print(
    words_sorting(
        'escape',
        'charm',
        'mythology'
  ))

output1
charm - 523
escape - 625
mythology - 1004

Comments:
All of the ascii values of the 'escape' word are:
e = 101, s = 115, c = 99, a = 97, p = 112, e = 101
Their sum is 625.
We add it in the dictionary {'escape': 625}.
The ascii values of the 'charm' are:
c = 99, h = 104, a = 97, r = 117, m = 109
Their sum is 523.
We add it in the dictionary {'escape': 625, 'charm': 625}
The ascii values of the 'mythology' word are:
m = 109, y = 121, t = 116, h = 104, o = 111, l = 108, o = 111, g = 103, y = 121.
Their sum is 1004.
We add it in the dictionary
{'escape': 625, 'charm': 523, 'mythology': 1004}
When we sum 625 + 523 + 1004 = 2152. The result is even, and we sort the dictionary by keys in ascending order.

Test Code2
print(
    words_sorting(
        'escape',
        'charm',
        'eye'
  ))

output2
escape - 625
charm - 523
eye - 323

Test Code3
print(
    words_sorting(
        'cacophony',
        'accolade'
  ))

output3
accolade - 812
cacophony - 964


"""

def words_sorting(*args):

    all_sum = 0
    dictionary = {}

    for words in args:
        sum = 0
        for letter in words:
            all_sum += ord(letter)
            sum += ord(letter)

        dictionary[words] = sum

    if all_sum % 2 == 0:
        sorted_result = [f'{key} - {value}' for key, value in sorted(dictionary.items(), key = lambda x: (x[0]))]

    else:
        sorted_result = [f'{key} - {value}' for key, value in sorted(dictionary.items(), key=lambda x: (-x[1]))]
    return "\n".join(sorted_result)

print(
    words_sorting(
        'escape',
        'charm',
        'mythology'
  ))



"""
        x = ord('a')
        print(x)

        text = 'charm'
        sum = 0
        for letter in text:
            sum += ord(letter)

        print(sum)
"""

"""
        text = 'escape'
        sum = 0
        for letter in text:
            sum += ord(letter)

        print(sum)
"""

