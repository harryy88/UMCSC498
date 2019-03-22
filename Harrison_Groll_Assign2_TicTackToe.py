# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import random


def HumanPlayer(Tag, Board):
    """Return choice of human player as tuple"""
    row = int(input("Enter a Row (0-2): "))
    col = int(input("Enter a Col (0-2): "))
    while not(0 <= col <= 2) and not(0 <= row <= 2) or (Board[row][col] == "X" or Board[row][col] == "O"):
        row = int(input("Enter a Row (0-2): "))
        col = int(input("Enter a Col (0-2): "))
    return (row, col)


def ComputerPlayer(Tag, Board):
    """Return choice of comp player as tuple"""
    row = col = 0
    while Board[row][col] == "X" or Board[row][col] == "O":
        row = random.randint(0,2)
        col = random.randint(0,2)
    return (row, col)


def Judge(Board):
    """0- Prog, 1- X, 2-O, 3-Tie"""
    if not IsSpaceFree(Board):
        return 3
    for i in range(3):
        if (Board[0][i] == Board[1][i] == Board[2][i] != " "):
            if Board[0][i] == "X":
                return 1
            else: 
                return 2
        
        if (Board[i][0] == Board[i][1] == Board[i][2] != " "):
            if Board[0][i] == "X":
                return 1
            else: 
                return 2
    if Board[0][0] == Board[1][1] == Board[2][2] != " ":
        if Board[0][0] == "X":
            return 1
        else: 
            return 2
    if Board[0][2] == Board[1][1] == Board[2][0] != " ":
        if Board[0][0] == "X":
            return 1
        else: 
            return 2
        
    return 0
    
def DrawBoard(Board):
    for i in range(3):
        for j in range(3):
            print(Board[i][j], "| ", end="")
            if j % 2 == 0 and j != 0:
                print()
                print("+++++++++++", end="")
        print()
    print("******************************")

def IsSpaceFree(Board):
    for row in range(3):
        for col in range(3):
            if Board[row][col] != "X" or Board[row][col] != "O":
                return True
    return False

def GoesFirst():
    x = random.randint(1,101)
    if x % 2 == 0: 
        print("Human Goes First (You are X)!!!")
        tag = "X"
    else: 
        print("Computer Goes First(You are X)!!!")
        tag = "O"
    return tag

def UpdateBoard(Board, move, tag):
    row = move[0]
    col = move[1]
    Board[row][col] = tag
    
    
def ShowOutCome(board, OutCome):
    if OutCome == 3:
        print("TIE GAME")
    elif OutCome == 1:
        print("X WINS :)")
    else:
        print("O WINS :)")

def TickTackToeGame():
    Board = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
    DrawBoard(Board)
    tag = GoesFirst()
    outcome = 0
    while outcome == 0:
        if tag == "X":
            move = HumanPlayer(tag, Board)
        else:
            move = ComputerPlayer(tag, Board)
        UpdateBoard(Board, move, tag)
        input("PRESS TO CONTINUE...")
        outcome = Judge(Board)
        DrawBoard(Board)
        tag = "X" if tag == "O" else "O"
    ShowOutCome(Board, outcome)

def PlayGame(): 
    while True: 
        TickTackToeGame()
        print("Do you want to play again? (yes/no)")
        if not input().lower().startswith('y'):
            break
        print("Game Over")

PlayGame()