"""
input1
1.0 2.5 3.0 4.5

output1
[1, 2, 3, 4]

input2
2.56 1.9 -3.4 8.1

output2
[3, 2, -3, 8]

"""
base_list = input().split(" ")
final_list = []

for n in base_list:
    final_n = round(float(n))
    final_list.append(final_n)


print(final_list)