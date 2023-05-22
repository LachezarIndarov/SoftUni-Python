"""
Simple two-player tic-tac-toe game.
| X |   |   |           | 1 | 2 | 3 |
| O | X |   |           | 4 | 5 | 6 |
| O |   | X |           | 7 | 8 | 9 |
X - wins
"""


def read_players():
    player_one_name = input('Player one name: ')
    player_two_name = input('Player two name: ')

    player_one_sign = input(f"{player_one_name} would you like to play with 'X' or 'O'? ").upper()
    while player_one_sign not in ['X', 'O']:
        player_one_sign = input(f"{player_one_name} would you like to play with 'X' or 'O'? ").upper()

    player_two_sign = 'O' if player_one_sign == 'X' else 'X'
    return [(player_one_name, player_one_sign), (player_two_name, player_two_sign)]


def print_board_numeration(board):
    print('This is the numeration of the board:')
    idx = 1
    for row in range(len(board)):
        print('|', end='')
        for col in range(len(board)):
            print(f'  {idx:02d}  |', end='')
            idx += 1
        print()


def get_position_mapping(board):
    result = {}
    idx = 1
    for row in range(len(board)):
        for col in range(len(board)):
            result[idx] = (row, col)
            idx += 1
    return result


def print_board(board):
    for row in range(len(board)):
        print('|', end='')
        for col in range(len(board)):
            print(f'  {" " if board[row][col] is None else board[row][col]}  |', end='')
        print()


def check_row(sign, player_row, board):
    for col in range(len(board)):
        if board[player_row][col] != sign:
            return False
    return True


def check_col(sign, player_col, board):
    for row in range(len(board)):
        if board[row][player_col] != sign:
            return False
    return True


def check_primary(sign, board):
    for idx in range(len(board)):
        if board[idx][idx] != sign:
            return False
    return True


def check_secondary(sign, board):
    for idx in range(len(board)):
        if board[idx][len(board) - 1 - idx] != sign:
            return False
    return True


def check_for_win(sign, player_row, player_col, board):
    return check_row(sign, player_row, board) or \
           check_col(sign, player_col, board) or \
           check_primary(sign, board) or \
           check_secondary(sign, board)


def is_draw(board):
    for row in range(len(board)):
        for col in range(len(board)):
            if board[row][col] is None:
                return False
    return True


def play_game(players, board, positions_mapping):
    print(f'{players[0][0]} starts first!')
    while True:
        player_name, player_sign = players[0]
        position_as_str = input(f'{player_name} choose a free position [1-{len(board) * len(board)}]: ')
        if not position_as_str.isdigit():
            print(f'{position_as_str} is not a valid integer position!')
            continue

        position = int(position_as_str)
        if position not in positions_mapping:
            print(f'{position} is not a valid position!')
            continue

        row, col = positions_mapping[position]
        if board[row][col] is not None:
            print(f'{position} is already selected!')
            continue

        board[row][col] = player_sign

        print_board(board)

        if check_for_win(player_sign, row, col, board):
            print(f'{player_name} won!')
            break

        if is_draw(board):
            print('draw!')
            break

        players[0], players[1] = players[1], players[0]


players = read_players()

board_size = 3
board = []
[board.append([None] * board_size) for _ in range(board_size)]

print_board_numeration(board)

positions_mapping = get_position_mapping(board)

play_game(players, board, positions_mapping)

