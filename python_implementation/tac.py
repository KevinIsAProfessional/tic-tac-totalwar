#!/usr/bin/env python3

from tkinter import *
from tkinter import ttk
import math

class Screen:
    global player 
    player = "X"
    def __init__(self,root):
        mainframe = ttk.Frame(root, padding=5)
        mainframe.grid(column=0, row=0)

        self.topMessageContents = StringVar()
        self.topMessageContents.set("X's turn")
        topMessage = ttk.Label(mainframe, textvariable=self.topMessageContents)
        topMessage.grid(column=0, row=0, columnspan=4, sticky=N)
        
        # What is the problem?
        # I want to dynamically generate the board BUT
        # I can't find a way to bind a text update to an individual button UNLESS
        # I hand create each StringVar, Button, and update function AND
        # That sucks

        board = Board(mainframe)


class Board:
    def __init__(self, parent):
        self.board = [[],[]]
        for i in range(9):
            self.board[0].append(StringVar(parent, value=""))
            self.board[1].append(ttk.Button(parent, textvariable=self.board[0][i], command=lambda i=i: self.changeOwner(i)))
            self.board[1][i].grid(column=(i%3), row=(math.floor(i/3)))


    def changeOwner(self, position):
        global player
        self.board[0][position].set(player)
        if player == "X":
            player = "O"
        else:
            player = "X"

    # An object that holds coordinates 
    # Gets passed as an argument to change stringVar?



def main():
    root = Tk()
    root.title("Tic Tac Toe")

    main = Screen(root)

    root.mainloop()

if __name__=="__main__":
    main()
