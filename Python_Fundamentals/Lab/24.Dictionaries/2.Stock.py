"""
input1
cheese 10 bread 5 ham 10 chocolate 3
jam cheese ham tomatoes

output1
Sorry, we don't have jam
We have 10 of cheese left
We have 10 of ham left
Sorry, we don't have tomatoes

input2
eggs 5 bread 10
bread eggs

output2
We have 10 of bread left
We have 5 of eggs left

"""


data = input().split(" ")
search_data = input().split(" ")
bakery = {}

for i in range(0, len(data), 2):
    food = data[i]
    quantity = int(data[i+1])
    bakery[food] = quantity

for search_term in search_data:
    if search_term in bakery.keys():
        print(f"We have {bakery[search_term]} of {search_term} left")
    else:
        print(f"Sorry, we don't have {search_term}")






