"""

input1
bread 10 butter 4 sugar 9 jam 12
output1
{'bread': 10, 'butter': 4, 'sugar': 9, 'jam': 12}


input2
eggs 3 sugar 7 salt 1 butter 3
output2
{'eggs': 3, 'sugar': 7, 'salt': 1, 'butter': 3}
"""

data = input().split(" ")
bakery = {}

for i in range(0, len(data), 2):
    food = data[i]
    quantity = int(data[i+1])

    bakery[food] = quantity

print(bakery)

