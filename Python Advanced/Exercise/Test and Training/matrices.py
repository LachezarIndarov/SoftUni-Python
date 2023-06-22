# list of n 0 - списък от "n" нули
list = []
n = 10

for i in range(n):
    list.append(0)

print(list) # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

#--------------------------------------------------------

# matric of NxM '0'
n = 5
m = 7

mm = []

for i in range(n):
    list = []

    for j in range(m):
        list.append(0)
    mm.append(list)

print(mm) # [[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]]

#--------------------------------------------------------------------

mm = []
for i in range(n):
    list = []

    for j in range(m):
        list.append(j)

    mm.append(list)

print(mm) # [[0, 1, 2, 3, 4, 5, 6], [0, 1, 2, 3, 4, 5, 6], [0, 1, 2, 3, 4, 5, 6], [0, 1, 2, 3, 4, 5, 6], [0, 1, 2, 3, 4, 5, 6]]

#-------------------------------------------------------------------------

# Create list 'n' zeros

n = 5
list = []

for i in range(n):
    list.append(0)

print(list) # [0, 0, 0, 0, 0]

#--------------------------------------------------------------------------


# create NxM matrix of zeros
n = 5
m = 3

mm = []

for i in range(n):
    list = []
    for j in range(m):
        list.append(0)
    mm.append(list)

print(mm) # [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]

# create NxM matrix of zeros
n = 5
m = 3

mm = []

for i in range(n):
    list = []
    for j in range(m):
        list.append(7)
    mm.append(list)

print(mm)  # [[7, 7, 7], [7, 7, 7], [7, 7, 7], [7, 7, 7], [7, 7, 7]]


