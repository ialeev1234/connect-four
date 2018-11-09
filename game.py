import itertools
import random

HEIGHT = 7
WIDTH = 6

players = ['1', '2']
board = [''] * WIDTH


def print_table():
    out = ''
    for i in range(HEIGHT):
        for j in range(WIDTH):
            out = (board[j][i:i+1] or 'O') + ' ' + out
        out = '\n' + out
    print(out)


def look_into_transparent(transparent):
    winner = None
    for trans in transparent:
        for p in players:
            if p * 4 in ''.join([t for t in trans if t]):
                winner = p
    return winner


def check_winner():
    winner = None
    filled_board = []
    # check verticals of table
    for b in board:
        filled_board.append(b.ljust(HEIGHT, 'O'))
        for p in players:
            if p * 4 in b:
                winner = p
    if not winner:
        # check horizontals of table
        winner = look_into_transparent(itertools.zip_longest(*filled_board))
    if not winner:
        # check growings of table
        transparented = itertools.zip_longest(*[b.rjust(HEIGHT + i, 'O') for i, b in enumerate(filled_board)])
        winner = look_into_transparent(transparented)
    if not winner:
        # check fallings of table
        filled_board.reverse()
        transparented = itertools.zip_longest(*[b.rjust(HEIGHT + i, 'O') for i, b in enumerate(filled_board)])
        winner = look_into_transparent(transparented)
    return winner


def is_valid(col):
    result = True
    if not col:
        print('\nEmpty input')
        result = False
    elif len(board[WIDTH - int(col)]) == HEIGHT:
        print('\nThis column already full')
        result = False
    return result


print_table()
while True:
    column = input('\nEnter column: ')
    if not is_valid(column):
        continue
    i = WIDTH - int(column)
    board[i] = board[i] + '1'
    winner = check_winner()
    if winner:
        print_table()
        print(f'\nWinner is {winner}')
        break
    while True:
        ai_column = random.choice(range(1, WIDTH + 1))
        i = WIDTH - int(ai_column)
        if is_valid(ai_column):
            break
    board[i] = board[i] + '2'
    print_table()
    winner = check_winner()
    if winner:
        print(f'\nWinner is {winner}')
        break
