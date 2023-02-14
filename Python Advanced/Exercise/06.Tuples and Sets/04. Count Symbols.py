"""
input1
SoftUni rocks

output1
: 1 time/s
S: 1 time/s
U: 1 time/s
c: 1 time/s
f: 1 time/s
i: 1 time/s
k: 1 time/s
n: 1 time/s
o: 2 time/s
r: 1 time/s
s: 1 time/s
t: 1 time/s

input2
Why do you like Python?

output2
: 4 time/s
?: 1 time/s
P: 1 time/s
W: 1 time/s
d: 1 time/s
e: 1 time/s
h: 2 time/s
i: 1 time/s
k: 1 time/s
l: 1 time/s
n: 1 time/s
o: 3 time/s
t: 1 time/s
u: 1 time/s
y: 3 time/s


"""

text = input()

symbols = {}
for ch in text:
    if ch in symbols:
        symbols[ch] += 1
    else:
        symbols[ch] = 1

for key,value in sorted(symbols.items()):
    print(f'{key}: {value} time/s')