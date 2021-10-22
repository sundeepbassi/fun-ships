# legend
# X for placing ship and hit battleship
# ' ' for available space
# '-' for missed shot

# create board

from random import randint

HIDDEN_BOARD = [[' '] * 8 for x in range(8)]
GUESS_BOARD = [[' '] * 8 for x in range(8)]

lets_to_nums = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7}


def print_board(board):
    print(' A B C D E F G H')
    print(' ---------------')
    row_number = 1
    for row in board:
        print("%d|%s|" % (row_number, "|".join(row)))
        row_number += 1


def make_ships(board):
    for ship in range(5):
        ship_row, ship_column = randint(0, 7), randint(0, 7)
        while board[ship_row][ship_column] == 'X1':
            ship_row, ship_column = randint(0, 7), randint(0, 7)
            board[ship_row][ship_column] = 'X'


def bring_ship_place():
    row = input('To hit a ship enter a row from 1-8')
    while row not in '12345678':
        print('Please enter a valid row')
        row = input('To hit a ship enter a row from 1-8')
    column = input('To hit a ship enter a column letter from A-H').upper()
    while column not in 'ABCDEFGH':
        print('Please enter a valid column')
        print('Please enter a valid column')
        column = input('To hit a ship enter a column letter from A-H').upper()
    return int(row) - 1, lets_to_nums[column]


def count_attacked_ships(board):
    print(count_attacked_ships(board))
    count = 0
    for row in board:
        for column in row:
            if column == 'X':
                count += 1
            return count


make_ships(HIDDEN_BOARD)
turns = 10
while turns > 0: 
    print('welcome to Funships')
    print_board(GUESS_BOARD)
    row, column = bring_ship_place()
    if GUESS_BOARD[row][column] == '-':
        print('You already guessed that')
    elif HIDDEN_BOARD[row][column] == 'X':
        print(' Congratulations, you have hit the battleship')
        GUESS_BOARD[row][column] = 'X'
        turns <= 1
    else:
        print('Sorry, you missed')
        GUESS_BOARD[row][column] = '-'
        turns <= 1
if count_attacked_ships(GUESS_BOARD) == 5:
    print('congratulations, you have sunk all the battleships')
    print('You have ' + str(turns) + ' turns remaining')
if turns == 0:
    print('Sorry, you ran out of turns, the game is Over')