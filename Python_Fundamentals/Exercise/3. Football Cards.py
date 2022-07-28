"""
input1
A-1 A-5 A-10 B-2

output1
Team A - 8; Team B - 10

input2
A-1 A-5 A-10 B-2 A-10 A-7 A-3

output2
Team A - 6; Team B - 10
Game was terminated


"""

SequenceOfCards = input().split(' ')

Team_A = 11
Team_B = 11

condition = False

player_loses = []

for card in SequenceOfCards:
    if card not in player_loses:
        player_loses.append(card)
        if 'A' in card:
            Team_A -= 1
        elif 'B' in card:
            Team_B -= 1

        if Team_A < 7 or Team_B < 7:
            condition = True
            break

print(f"Team A - {Team_A}; Team B - {Team_B}")

if condition:
    print("Game was terminated")