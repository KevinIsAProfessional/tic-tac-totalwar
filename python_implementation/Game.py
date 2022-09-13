from tkinter import *
from tkinter import ttk
import Boards, Players

class Game(ttk.Frame):
    def __init__(self, parent, wm):
        super().__init__(parent)
        self.wm = wm
        wm.setSize("welcome")

        self.parent = parent
        self.players = Players.Players()
        self.gameType = "battle"

        self.bannerMessage = StringVar(self, "Tic Tac Totalwar")
        self.banner = ttk.Label(self,textvariable=self.bannerMessage)
        self.banner.grid(column=0, row=0)

        self.messageFrame = ttk.Frame(self)

    def welcomeMessage(self):
        self.wm.setSize("welcome")
        self.messageFrame.grid(column=0, row=1)
        self.battleButton = ttk.Button(self.messageFrame, text="Fight Battle", command=self.battle) 
        self.warButton = ttk.Button(self.messageFrame, text="Start War", command=self.war)
        self.battleButton.grid(column=0, row=0)
        self.warButton.grid(column=1, row=0)

    def retryMessage(self):
        self.wm.addRetry()
        self.messageFrame.grid(column=0, row=2)
        self.battleButton.destroy()
        self.warButton.destroy()
        self.retryButton = ttk.Button(self.messageFrame, text="Play again?", command=self.reset)
        self.retryButton.grid(column=0, row=0, columnspan=2)

    def reset(self):
        self.retryButton.destroy()
        self.board.destroy()
        self.updateBanner("reset")
        self.welcomeMessage()

    def battle(self):
        self.wm.setSize("battle")
        self.gameType = "battle"
        self.board = Boards.BattleBoard(self, self.players)
        self.board.grid(column=0, row=1)
        self.board.initializeBoard()

    def war(self):
        self.wm.setSize("war")
        self.gameType = "war"
        self.board = Boards.WarBoard(self, self.players)
        self.board.grid(column=0, row=1)
        self.board.initializeBoard()

    def processMove(self, win, pos, boardId):
        if self.gameType == "battle":
            if win:
                self.updateBanner("win")
                self.retryMessage()
            else:
                self.players.switchPlayer()
                self.board.enableBoard()
                self.updateBanner("next")
        else:
            if win:
                self.updateBanner("win")
                self.retryMessage()
            else:
                self.players.switchPlayer()
                self.updateBanner("next")

    def updateBanner(self, messageType):
        if messageType == "next":
            self.bannerMessage.set(f"{self.players.getActivePlayer()}'s turn")
        elif messageType == "win":
            self.bannerMessage.set(f"{self.players.getActivePlayer()} wins!")
        elif messageType == "reset":
            self.bannerMessage.set("Tic Tac Totalwar")

class WindowManager:
    def __init__(self, root):
        self.root = root
        self.type = "welcome"
        self.welcomeScreen = "185x50"
        self.battleScreen = "290x120"
        self.retryBattleScreen = "290x150"
        self.warScreen = "875x325"
        self.retryWarScreen = "875x355"

    def addRetry(self):
        if self.type == "battle":
            self.root.geometry(self.retryBattleScreen)
        elif self.type == "war":
            self.root.geometry(self.retryWarScreen)

    def setSize(self, screenType):
        self.type = screenType
        if self.type == "welcome":
            self.root.geometry(self.welcomeScreen)
        elif self.type == "battle":
            self.root.geometry(self.battleScreen)
        elif self.type == "war":
            self.root.geometry(self.warScreen)
            


def main():
    root = Tk()
    root.title("Tic Tac Totalwar")

    wm = WindowManager(root)

    game = Game(root, wm)
    game.grid(row=0, column=0)
    game.welcomeMessage()

    root.mainloop()

if __name__=="__main__":
    main()
