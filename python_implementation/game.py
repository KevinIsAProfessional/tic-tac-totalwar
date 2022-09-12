from tkinter import *
from tkinter import ttk
import Boards, Players

class Game(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.players = Players.Players()
        self.gameType = "oneBoard"

        self.bannerMessage = StringVar(self, "Tic Tac Totalwar")
        self.banner = ttk.Label(self,textvariable=self.bannerMessage)
        self.banner.grid(column=0, row=0)

    def oneBoard(self):
        self.gameType = "oneBoard"
        self.board = Boards.BattleBoard(self, self.players)
        self.board.grid(row=1, column=0)
        self.board.initializeBoard()

    def nineBoard(self):
        self.gameType = "nineBoard"
        self.board = Boards.WarBoard(self, self.players)
        self.board.grid(row=1, column=0)
        self.board.initializeBoard()

    def processMove(self, win, pos, boardId):
        if self.gameType == "oneBoard":
            if win:
                self.updateBanner("win")
            else:
                self.players.switchPlayer()
                self.board.enableBoard()
                self.updateBanner("next")
        else:
            if win:
                self.updateBanner("win")
            else:
                self.players.switchPlayer()
                self.updateBanner("next")

    def updateBanner(self, messageType):
        if messageType == "next":
            self.bannerMessage.set(f"{self.players.getActivePlayer()}'s turn")
        elif messageType == "win":
            self.bannerMessage.set("Game over")


def main():
    root = Tk()
    root.title("Tic Tac Totalwar")

    game = Game(root)
    game.grid(row=0, column=0)
    game.nineBoard()

    root.mainloop()

if __name__=="__main__":
    main()
