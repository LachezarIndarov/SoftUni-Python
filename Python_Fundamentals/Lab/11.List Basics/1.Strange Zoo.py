"""
input1
my tail
my body seems on place
my head is on the wrong end!

output1
['my head is on the wrong end!', 'my body seems on place', 'my tail']

input2
tail
body
head

output2
['head', 'body', 'tail']

"""

tail = input()
body = input()
head = input()


meerkat = [tail, body, head]

meerkat[0], meerkat[2] = meerkat[2], meerkat[0]

print(meerkat)

