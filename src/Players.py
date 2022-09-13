
class Players:
    class Player:
        def __init__(self, token):
            self.token = token
            #self.color = color

        def getToken(self):
            return self.token


    def __init__(self):
        self.player1 = self.Player("X")
        self.player2 = self.Player("O")
        self.activePlayer = self.player1 
        
    def getActivePlayer(self):
        return self.activePlayer.getToken()

    def switchPlayer(self):
        self.activePlayer = self.player1 if self.activePlayer == self.player2 else self.player2 
        #self.banner.updateBanner(f"{self.activePlayer.getToken()}'s turn")
