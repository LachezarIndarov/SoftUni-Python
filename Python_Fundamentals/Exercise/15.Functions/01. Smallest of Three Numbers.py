"""
input1
2
5
3

output1
2

input2
600
342
123

output2
123

input3
25
21
4

output3
4

"""
a = int(input())
b = int(input())
c = int(input())

def numbers(a,b,c):
    if a < b and a < c:
        return(a)
    elif b < a and b < c:
        return(b)
    elif c < a and c < b:
        return(c)


print(numbers(a,b,c))
