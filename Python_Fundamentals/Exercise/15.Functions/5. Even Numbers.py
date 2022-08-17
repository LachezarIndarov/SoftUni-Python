"""
input1
1 2 3 4

output1
[2, 4]

input2
1 2 3 -1 -2 -3

output2
[2, -2]

"""
result = list(filter(lambda x: x % 2 == 0,list(map(int,input().split(' ')))))
print(result)







