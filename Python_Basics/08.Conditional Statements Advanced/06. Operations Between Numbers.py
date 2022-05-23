"""
input1
10
12
+

output1
10 + 12 = 22 - even

input2
10
1
-

output2
10 - 1 = 9 - odd

input3
7
3
*


output3
7 * 3 = 21 - odd

input4
123
12
/

output4
123 / 12 = 10.25

input 5
10
3
%

output5
10 % 3 = 1

input6
112
0
/

output6
Cannot divide 112 by zero

input7
10
0
%

output7
Cannot divide 10 by zero

"""
#GitHub  - 100% Judge

N1 = int(input())
N2 = int(input())
operator = str(input())

result = 0


if operator == '+' or operator == '-' or operator == '*' :

    if operator == '+':
        result = N1 + N2
    elif operator == '-':
        result = N1 - N2
    elif operator == '*':
        result = N1 * N2

    if result % 2 == 0:
        print(f"{N1} {operator} {N2} = {result} - even")
    else:
        print(f"{N1} {operator} {N2} = {result} - odd")

elif operator == '/' or operator == '%':
    if N2 == 0:
        print(f"Cannot divide {N1} by zero")
    elif operator =='/':
        result = N1 / N2
        print(f"{N1} / {N2} = {result:.2f}")
    elif operator =='%':
        result = N1 % N2
        print(f"{N1} % {N2} = {result}")





