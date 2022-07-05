"""
input1
16
20
46
12
8
20
49
Christmas

output1
Number of adults: 4
Number of kids: 3
Money for toys: 15
Money for sweaters: 60

input2
16
16
16
16
16
Christmas

output2
Number of adults: 0
Number of kids: 5
Money for toys: 25
Money for sweaters: 0

input3
18
20
48
45
56
37
12
14
Christmas

output3
Number of adults: 6
Number of kids: 2
Money for toys: 10
Money for sweaters: 90

"""
years = input()
price_toy = 5
price_pullover = 15
num_kids = 0
num_adults = 0
price_toys = 0
price_pullovers = 0

while years != "Christmas":
    if int(years) <= 16:
        num_kids += 1
    else:
        num_adults += 1
    years = input()
price_toys = num_kids * price_toy
price_pullovers = num_adults * price_pullover

print(f"Number of adults: {num_adults}")
print(f"Number of kids: {num_kids}")
print(f"Money for toys: {price_toys}")
print(f"Money for sweaters: {price_pullovers}")


