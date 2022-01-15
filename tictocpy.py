## Tic Tac Py Game
## Jan 2022
## KGP

"""
[-,-,-],
[-,-,-],
[-,-,-]

1) user_input -> 1-9
2) if enter anything else, tell user to go again
3) check if user input is already placed
4) add it to the board
5) check if user won: check rows, columns, and diagonals
6) toggle between users and successful moves
"""

import numpy as np
import random as rando

board = [
    [ "-", "-", "-" ],
    [ "-", "-", "-" ],
    [ "-", "-", "-" ]
]

user = True 

def print_board(board):
    for row in board:
        for place in row:
            print(f"{place} ", end= "")
        print()

def quit(user_input):
    if user_input == "q":
        print("\n Thanks for playing")
        return True
    else:
        return False

def check_input(user_input):
    # check first if number
    if not isnumber(user_input): return False
    user_input = int(user_input)
    # check if its 1-9
    if not bounds(user_input): return False
    return True

def isnumber(user_input):
    if not user_input.isnumeric():
        print("this is not valid position")
        return False
    else:
        return True

def bounds(user_input):
    if (user_input < 1) or (user_input > 9):
        print("This number is out of bounds")
        return False
    else: return True

def istaken(coords, board):
    row = coords[0]
    col = coords[1]
    if board[row][col] != '-':
        print("Position already taken")
        return True
    else: return False

def coordinates(user_input):
    row = int(user_input / 3)
    col = user_input 
    if col > 2: col = int(col % 3)
    return (row, col)

def addToBoard(coords, board, player):
    row = coords[0]
    col = coords[1]
    board[row][col] = player

def randomCoords(board, player):

    while True:
        available = [0,1,2,3,4,5,6,7,8]
        select = rando.choice(available)
        randomCoords = coordinates(select)
        coords = randomCoords
        row = coords[0]
        col = coords[1]
        if board[row][col] != '-':
            return True      
        else: break

    row = coords[0]
    col = coords[1]
    board[row][col] = player


def current_user(user):
    if user : return "x"
    else: return 'o'

def winner(user, board):
    if check_row(user, board): return True
    if check_col(user, board): return True
    if check_diag(user, board): return True
    return False


def check_row(user, board):
    for row in board:
        complete_row = True
        for place in row:
            if place != user:
                complete_row = False
                break
        if complete_row: return True
    return False

def check_col(user, board):
    for col in range(3):
        complete_col = True
        for row in range(3):
            if board[row][col] != user:
                complete_col = False
                break
        if complete_col: return True
    return False

def check_diag(user, board):
    if board[0][0] == user and board[1][1] == user and board[2][2] == user:
        return True
    elif board[0][2] == user and board[1][1] == user and board[2][0] == user:
        return True
    else: return False

while True:
    
    player = current_user(user)
    print_board(board)
    user_input = input("Please enter a number between 1-9 to indicate player move: ")
    if quit(user_input): break
    if not check_input(user_input):
        print("Please try again")
        continue
    user_input = int(user_input) - 1
    coords = coordinates(user_input)
    if istaken(coords, board):
        print("Please try again.")
        continue
    addToBoard(coords, board, player)
    randomCoords(board,'o')
        
    if winner(player, board):
        print(f"\n {player.upper()} is the winner! \n")
        break

    user = not user

   
        