from tkinter import *
from tkinter import ttk
import math



class Board(ttk.Frame):
    def __init__(self, parent, players, boardId):
        self.style = ttk.Style()
        self.style.configure("Inactive.TFrame", padding=1, background="#CF9817")
        self.style.configure("Active.TFrame", padding=2, background="#026633")
        super().__init__(parent, padding=4)
        self.parent = parent
        self.players = players
        self.boardArray = []
        self.owners     = []
        self.boardId    = boardId
        self.size       = 3
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

    def checkForWin(self):
        for combo in self.winningCombos:
            one = self.owners[combo[0]]
            two = self.owners[combo[1]]
            three = self.owners[combo[2]]
            if one != "":
                if one == two and one == three:
                    self.owner = one
                    return True
        if "" not in self.owners:
            return True
        return False

    def getSize(self):
        return self.size ** 2


class BattleBoard(Board):
    def __init__(self, parent, players, boardId=0):
        super().__init__(parent, players, boardId)
        self.stringVars = []
        self.hasOwner = False
        self.frame = ttk.Frame(self, padding=3)
        self.frame.grid(column=0, row=0)
        self.frame["style"] = "Active.TFrame"
        self.initializeBoard()

    def initializeBoard(self):
        for i in range(self.getSize()):
            self.owners.append("")
            self.stringVars.append(StringVar(self, self.owners[i]))
            self.boardArray.append(ttk.Button(self.frame, textvariable=self.stringVars[i], command=lambda i=i: self.processMove(i)))
            self.boardArray[i].grid(column=(i%self.size), row=(math.floor(i/self.size)))

    def processMove(self, pos):
        token = self.players.getActivePlayer()
        self.owners[pos] = token
        self.updateStringVar(pos)
        self.disableBoard()
        if self.checkForWin():
            self.hasOwner = True
            self.parent.processMove(True, pos, self.boardId)
        else:
            self.parent.processMove(False, pos, self.boardId)

    def updateStringVar(self, pos):
        self.stringVars[pos].set(self.owners[pos])

    def disableBoard(self):
        for button in self.boardArray:
            button["state"] = DISABLED
            self.frame["style"] = "Inactive.TFrame"

    def enableBoard(self):
        if not self.hasOwner:
            for i, square in enumerate(self.owners):
                if square == "":
                    self.boardArray[i]["state"] = NORMAL
                    self.frame["style"] = "Active.TFrame"

class WarBoard(Board):
    def __init__(self, parent, players, boardId=0):
        super().__init__(parent, players, boardId)
        self.activeBoard = None

    def initializeBoard(self):
        for i in range(self.getSize()):
            self.owners.append("")
            self.boardArray.append(BattleBoard(self, self.players, i))
            self.boardArray[i].grid(column=(i%self.size), row=(math.floor(i/self.size)))

    def processMove(self, win, pos, boardId):
        if win:
            self.owners[boardId] = self.players.getActivePlayer()
            if self.checkForWin():
                self.parent.processMove(True, pos, boardId)
                return None
        if self.owners[pos] != "":
            self.activeBoard = None
            for board in self.boardArray:
                self.activateBoards()
            self.parent.processMove(False, pos, boardId)
        else:
            self.activeBoard = pos
            self.activateBoards()
            self.parent.processMove(False, pos, boardId)

    def activateBoards(self):
        if self.activeBoard == None:
            for board in self.boardArray:
                board.enableBoard()
        else:
            for i,board in enumerate(self.boardArray):
                if i != self.activeBoard:
                    board.disableBoard()
                else:
                    board.enableBoard()
