"""
input1
kiwi orange banana apple

output1
kiwi
orange
banana

input2
pizza cake pasta chips

output2
cake

"""

text = input().split(" ")
even =[x for x in text if (len(x) % 2 == 0)]
print('\n'.join(even))


