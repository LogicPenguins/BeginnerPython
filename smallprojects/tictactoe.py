#! python3
# tictactoe.py - A simple tic-tac-toe game
# Author: Xmexy

import pyinputplus as pyip
import sys
import random
import time

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

# This function will take either 'x' or 'o' as the player and board as parameter. This function will allow input from a human player
def handle_player(player, board_param):
    print(f"It is {player}'s turn. Please choose a number from 1-9 on a non-claimed square.")
    player_turn_done = False

    while player_turn_done != True:
        try:
            player_move = pyip.inputInt('Move: ', min=1, max=9, timeout=60)
            if board_param[f'{player_move}'] == ' ':
                board_param[f'{player_move}'] = player
                player_turn_done = True
            else:
                print('That square is already taken! Try again.')
                continue

        except TimeoutError:
            print('Input took too long to receive. Please restart the program.')
            sys.exit()

# This function will take either 'x' or 'o' as the player and board as parameter. This function will automatically play as AI
def handle_ai(player, board_param):
  player_turn_done = False

  while player_turn_done != True:
    ai_move = random.randint(1, 9)
    if board_param[f'{ai_move}'] == ' ':
      board_param[f'{ai_move}'] = player
      player_turn_done = True
    else:
      continue

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

# Main game loop (currently both set to AI. Calling the function handle_player rather than handle_ai will allow players to participate)
while True:

    # X goes first. Handle X's turn. 
    handle_player('X', board)
    turns_taken += 1
    board_print(board)
    check_for_winner(board, 'X')

    if turns_taken == 9:
        break
    time.sleep(1)

    # O goes second. Handle O's turn. 
    handle_ai('O', board)
    turns_taken += 1
    board_print(board)
    check_for_winner(board, 'O')

    if turns_taken == 9:
        break
    time.sleep(1)

print('Game over. No one won.')