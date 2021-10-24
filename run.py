import random

playerLetter = 'X'
computerLetter = 'O'

# define the board
board = [' ' for i in range(10)]


# print the board
def print_board():
  print('#########################')
  print(board[1] + '|' + board[2] + '|' + board[3])
  print('----------')
  print(board[4] + '|' + board[5] + '|' + board[6])
  print('----------')
  print(board[7] + '|' + board[8] + '|' + board[9])


# is the board full
def is_full():
  return ' ' not in board[1:10]
 
# check if there is a winner
def check_win(board, letter):
  return (board[1] == board[2] == board[3] == letter) or \
         (board[4] == board[5] == board[6] == letter) or \
         (board[7] == board[8] == board[9] == letter) or \
         (board[1] == board[4] == board[7] == letter) or \
         (board[2] == board[5] == board[8] == letter) or \
         (board[3] == board[6] == board[9] == letter) or \
         (board[1] == board[5] == board[9] == letter) or \
         (board[3] == board[5] == board[7] == letter) 


