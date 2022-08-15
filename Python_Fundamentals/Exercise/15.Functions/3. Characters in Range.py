"""
input1
a
d

output1
b c

input2
#
:

output2
$ % & ' ( ) * + , - . / 0 1 2 3 4 5 6 7 8 9

input3
#
C

output3
$ % & ' ( ) * + , - . / 0 1 2 3 4 5 6 7 8 9 : ; < = > ? @ A B
"""
def char_in_range(ch1, ch2):

    result = []
    for i in range(ord(ch1) + 1, ord(ch2)):
        result.append(chr(i))

    print(' '.join(result))



char1 = input()
char2 = input()
char_in_range(char1, char2)
