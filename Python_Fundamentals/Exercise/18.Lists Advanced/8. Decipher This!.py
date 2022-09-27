"""
input1
72olle 103doo 100ya

output1
Hello good day

input2
82yade 115te 103o

output2
Ready set go

"""
text = input().split()


def swap(c, i, j):
    c = list(c)
    x=c[i]
    c[i], c[j] = c[j], x
    return "".join(c)

res=[]

for key in text:
    list_zero = []
    list_element = []
    [list_zero.append(i) for i in key if i.isdigit()]
    num = int("".join(list_zero))
    num = chr(num)
    list_element.insert(0,num)
    [list_element.append(j) for j in key if not j.isdigit()]

    res.append(swap(list_element, 1, - 1))
    res.append(" ")
    list_zero.clear();
    list_element.clear();

res="".join(res)

print(res)