"""
input1
a b c d e f g h
5

output1
['a', 'c', 'e', 'g', 'b', 'd', 'f', 'h']

input2
one two three four
3

output2
['one', 'three', 'two', 'four']

"""

cards = input().split()
count_shuffle = int(input())

lenght_teste = len(cards)
shuffle_faro = int(lenght_teste / 2)

for i in range(0,count_shuffle):
    list_cards =[]

    for j in range(0,shuffle_faro):
        list_cards.append(cards[j])
        list_cards.append(cards[shuffle_faro])
        shuffle_faro += 1

    cards = list_cards
    shuffle_faro = int(lenght_teste / 2)

print(list_cards)

