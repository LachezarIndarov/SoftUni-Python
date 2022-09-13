"""
input 1
arp, live, strong
lively, alive, harp, sharp, armstrong

output1
['arp', 'live', 'strong']

input2
tarp, mice, bull
lively, alive, harp, sharp, armstrong

output2
[]

"""

substrings = input().split(', ')
sentence = input()
result = [ i for i in substrings if i in sentence]

print(result)
