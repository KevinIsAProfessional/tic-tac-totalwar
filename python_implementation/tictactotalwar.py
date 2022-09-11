#!/usr/bin/env python3

from tkinter import *
from tkinter import ttk
import math

class Players:
    def __init__(self, ):
        self.activePlayer = "X"
        
    def getActivePlayer(self):
        return self.activePlayer

    def switchPlayer(self):
        self.activePlayer = "X" if self.activePlayer == "O" else "O"
        # FIXME: self.updateMessage()

class Board():
    def __init__(self, parent, players):
        self.parent = parent
        self.players = players
        self.boardArray = self.resetBoard()
        self.winningCombos = [
                            [0,1,2],
                            [3,4,5],
                            [6,7,8],
                            [0,3,6],
                            [1,4,7],
                            [2,5,8],
                            [0,4,8],
                            []
                        ]
        

    def resetBoard(self):
        boardArray = [[], [], []]
        for i in range(9):
            owner = StringVar(self.parent, value="") 
            boardArray[0].append(owner)

            button = ttk.Button(self.parent,
                                textvariable=boardArray[0][i],
                                command=lambda i=i: self.processMove(i))
            boardArray[1].append(button)
            boardArray[1][i].grid(column=(i%3+1), row=(math.floor(i/3)+1))
        return boardArray 

    def disableBoard(self):
        for button in self.boardArray[1]:
            button["state"] = DISABLED

    def enableBoard(self):
        for i in range(9):
            if i not in self.boardArray[2]:
                button =self.boardArray[1][i]
                button["state"] = NORMAL 

    def processMove(self, pos):
        self.boardArray[0][pos].set(self.players.getActivePlayer())
        self.boardArray[2].append(pos)
        self.disableBoard()
        if self.checkForWin():
            print("winner")
            self.disableBoard()
        else:
            self.enableBoard()
            self.players.switchPlayer()

    def checkForWin(self):
        for i in range(7):
            one = self.boardArray[0][self.winningCombos[i][0]].get()
            two = self.boardArray[0][self.winningCombos[i][1]].get()
            three = self.boardArray[0][self.winningCombos[i][2]].get()
            if (one != "") and (one == two) and (one == three):
                return True
        for string in self.boardArray[0]:
            if string.get() == "":
                return False
        else:
            print("cat's game")
            return False

class Game:
    def __init__(self, parent, gameMode):
        players = Players()
        if gameMode == 1:
            board = Board(parent, players)
        if gameMode == 9:
            pass
            

def main():
    root = Tk()
    root.title("Tic Tac Toe")

    mainframe = ttk.Frame(root, padding=5)
    mainframe.grid(column=0, row=0)

    players = Players()
    game = Board(mainframe, players)

    root.mainloop()

if __name__=="__main__":
    main()

