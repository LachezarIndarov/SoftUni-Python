
board = []
player_one, player_two = input().split(", ")


rows_count = 6
column_counts = 6

for i in range(rows_count):
    elements = list(input().split())
    board.append(elements)

winner = False

player_one_rest = False
player_two_rest = False

while True:
    row, col = eval(input())


    if not player_one_rest:
        player_move = board[row][col]
        if player_move == "E":
            print(f"{player_one} found the Exit and wins the game!")
            have_winner = True
            break

        elif player_move == "T":
            print(f"{player_one} is out of the game! The winner is {player_two}.")
            have_winner = True
            break

        elif player_move == "W":
            print(f"{player_one} hits a wall and needs to rest.")
            player_one_rest = True

    else:
        player_one_rest = False

    if winner:
        break

    player_one, player_two = player_two, player_one
    player_one_rest, player_two_rest = player_two_rest, player_one_rest