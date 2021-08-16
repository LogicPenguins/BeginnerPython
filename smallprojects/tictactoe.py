#! python3
# tictactoe.py - A simple tic-tac-toe game
# Author: Xmexy

import pyinputplus as pyip
import sys

print(f"\n{('━' * 140)}\n{(' ' * 60)}Tic-Tac-Toe\n{('━' * 140)}\n")

board = {
    '1': ' ', '2': ' ', '3': ' ',
    '4': ' ', '5': ' ', '6': ' ',
    '7': ' ', '8': ' ', '9': ' '
}


def board_print(board_param):
    print('\nCurrent Board: \n')
    print(f"{board_param['1']}|{board_param['2']}|{board_param['3']}")
    print('-+-+-')
    print(f"{board_param['4']}|{board_param['5']}|{board_param['6']}")
    print('-+-+-')
    print(f"{board_param['7']}|{board_param['8']}|{board_param['9']}")


def handle_turn(player, board_param):
    print(f"It is {player}'s turn. Please choose a number from 1-9 on a non-claimed square.")
    player_turn_done = False

    while player_turn_done != True:
        try:
            move = pyip.inputInt('Move: ', min=1, max=9, timeout=60)
            if board_param[f'{move}'] == ' ':
                board_param[f'{move}'] = player
                player_turn_done = True
            else:
                print('That square is already taken! Try again.')
                continue

        except TimeoutError:
            print('Input took too long to receive. Please restart the program.')
            sys.exit()

def check_for_winner(board_param, player):

    # Horizontal win for first row
    if board_param['1'] == player:
      if board_param['2'] == player:
         if board_param['3'] == player:
            print(f'{player} won the game!')
            sys.exit()

    # Horizontal win for second row
    if board_param['4'] == player:
      if board_param['5'] == player:
         if board_param['6'] == player:
            print(f'{player} won the game!')
            sys.exit()

    # Horizontal win for third row
    if board_param['7'] == player:
      if board_param['8'] == player:
         if board_param['9'] == player:
            print(f'{player} won the game!')
            sys.exit()
    
    # Vertical win for first column
    if board_param['1'] == player:
      if board_param['4'] == player:
         if board_param['7'] == player:
            print(f'{player} won the game!')
            sys.exit()
    
    # Vertical win for second column
    if board_param['2'] == player:
      if board_param['5'] == player:
         if board_param['8'] == player:
            print(f'{player} won the game!')
            sys.exit()

    # Vertical win for third column
    if board_param['3'] == player:
      if board_param['6'] == player:
         if board_param['9'] == player:
            print(f'{player} won the game!')
            sys.exit()

    # Diagonal win from top left to bottom right
    if board_param['1'] == player:
      if board_param['5'] == player:
         if board_param['9'] == player:
            print(f'{player} won the game!')
            sys.exit()
    
    # Diagonal win from bottom left to top right
    if board_param['7'] == player:
      if board_param['5'] == player:
         if board_param['3'] == player:
            print(f'{player} won the game!')
            sys.exit()
# Print out the current board
board_print(board)

# Tracker for how many turns have been taken
turns_taken = 0

# Main game loop
while True:

    # X goes first. Handle X's turn. 
    handle_turn('X', board)
    turns_taken += 1
    board_print(board)
    check_for_winner(board, 'X')

    if turns_taken == 9:
        break

    # O goes second. Handle O's turn. 
    handle_turn('O', board)
    turns_taken += 1
    board_print(board)
    check_for_winner(board, 'O')

    if turns_taken == 9:
        break

print('Game over. No one won.')