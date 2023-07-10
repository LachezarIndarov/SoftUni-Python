x,y,z = (1,2,3)

print(x) # 1
print(y) # 2
print(z) # 3

ll = list(range(5,16))

# Here, index, value in unpacking of tuple
for (index, value) in enumerate(ll):
    print(f'll[{index}] = {value}')

for index in range(len(ll)):
    value = ll[index]
    print(f'll[{index}] = {value}')

"""
ll[0] = 5
ll[1] = 6
ll[2] = 7
ll[3] = 8
ll[4] = 9
ll[5] = 10
ll[6] = 11
ll[7] = 12
ll[8] = 13
ll[9] = 14
ll[10] = 15
ll[0] = 5
ll[1] = 6
ll[2] = 7
ll[3] = 8
ll[4] = 9
ll[5] = 10
ll[6] = 11
ll[7] = 12
ll[8] = 13
ll[9] = 14
ll[10] = 15

"""
dictionary  = {

    'one': 1,
    'two': 2,
    'three':3,
}

# Here dictionaris - key, value is unpacking of tuple
for key,value in dictionary.items():
    print(f'd[{key}] = {value}')  #d[one] = 1
                                  #d[two] = 2
                                  #d[three] = 3

print(dictionary.items()) # dict_items([('one', 1), ('two', 2), ('three', 3)])
print(dictionary.items()) # dict_items([('one', 1), ('two', 2), ('three', 3)])
print(dictionary.items()) # dict_items([('one', 1), ('two', 2), ('three', 3)])
print(dictionary.items()) # dict_items([('one', 1), ('two', 2), ('three', 3)])
print(dictionary.items())
print(dictionary.items())
print(dictionary.items())
print(dictionary.items())


# Unpacking works for lists too
ll = ['one', 'two','three','four']

a,b,c,d = ll
print(a) # one
print(b) # two
print(c) # three
print(d) # four