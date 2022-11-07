"""
input1
bread: 4
cheese: 2
ham: 1
bread: 1
statistics

output1
Products in stock:
- bread: 5
- cheese: 2
- ham: 1
Total Products: 3
Total Quantity: 8


input2
eggs: 10
bread: 6
cheese: 8
milk: 7
statistics


output2
Products in stock:
- eggs: 10
- bread: 6
- cheese: 8
- milk: 7
Total Products: 4
Total Quantity: 31

"""
text = input()
store = {}

while text != "statistics":

    text = text.split(": ")
    product = text[0]
    quantity = int(text[1])

    if product in store.keys():
        store[product] += quantity
    else:
        store[product] = quantity

    text = input()

count = len(store.keys())
total = sum(store.values())

print("Products in stock:")
for product in store:
    print(f"- {product}: {store[product]}")

print(f"Total Products: {count}")
print(f"Total Quantity: {total}")
