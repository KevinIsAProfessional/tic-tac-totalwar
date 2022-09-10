#!/usr/bin/env python3

from tkinter import *
from tkinter import ttk
import math

class Players:
    def __init__(self, p1="X", p2="O"):
        self.player_one = p1
        self.player_two = p2
        self.active_player = p1

    def playMove(self):
        if self.active_player == self.player_one:
            self.active_player = self.player_two
            return self.player_one
        else:
            self.active_player = self.player_one
            return self.player_two


class Screen:
    # This seems kind of useless right now, maybe it can be home for the menu bar
    # Otherwise, maybe the mainframe and players can be moved to the main
    def __init__(self,root):
        pass



class Board:
    def __init__(self, parent, players):
        self.winningCombos = [
                            [0,1,2],
                            [3,4,5],
                            [6,7,8],
                            [0,3,6],
                            [1,4,7],
                            [2,5,8],
                            [0,4,8],
                            [2,4,6]
                ]
        self.parent = parent
        self.players = players

        self.topMessageContents = StringVar()
        self.updateMessage()
        self.topMessage = ttk.Label(parent, textvariable=self.topMessageContents)
        self.topMessage.grid(column=0, row=0, columnspan=4, sticky=N)

        self.board = [[],[]]
        for i in range(9):
            self.board[0].append(StringVar(parent, value=""))
            self.board[1].append(ttk.Button(parent, textvariable=self.board[0][i], command=lambda i=i: self.changeOwner(i)))
            self.board[1][i].grid(column=(i%3+1), row=(math.floor(i/3)+1))


    def checkForWin(self):
        for combo in self.winningCombos:
            if self.board[0][combo[0]].get() != "" and (self.board[0][combo[0]].get() == self.board[0][combo[1]].get()) and self.board[0][combo[0]].get() == self.board[0][combo[2]].get():
                return True
        return False

    def changeOwner(self, position):
        self.board[0][position].set(self.players.playMove())
        self.board[1][position]["state"] = DISABLED
        if self.checkForWin():
            self.winState()
        else:
            self.updateMessage()

    def winState(self):
        for button in self.board[1]:
            button["state"] = DISABLED
        self.topMessageContents.set(f"{self.players.active_player} loses!")

    def updateMessage(self):
        self.topMessageContents.set(f"{self.players.active_player}'s turn")

    # An object that holds coordinates
    # Gets passed as an argument to change stringVar?



def main():
    root = Tk()
    root.title("Tic Tac Toe")

    mainframe = ttk.Frame(root, padding=5)
    mainframe.grid(column=0, row=0)

    players = Players()
    board = Board(mainframe, players)

    root.mainloop()

if __name__=="__main__":
    main()
