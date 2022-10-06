import random

class RockPaperScissors:
    def __init__(self, playerMove):
        self.playerMove = playerMove
        self.opponentMove = ''

    def rockPaperScissors(self):
        __possibleMoves = ["scissors", 'rock', 'paper']

        for i in range(random.randint(1, 3)):
            self.opponentMove = __possibleMoves[i]

        if playerMove != None:
            if self.opponentMove == self.playerMove:
                return "draw"

            elif self.playerMove == 'scissors' and self.opponentMove == 'paper':
                return "win"
            elif self.playerMove == 'paper' and self.opponentMove == 'rock':
                return "win"
            elif self.playerMove == 'rock' and self.opponentMove == 'scissors':
                return "win"
            else:
                return "loose"

playerMove = input('Welcome to Epic Rock Paper Scissors! ').lower()
rps = RockPaperScissors(playerMove)

print(rps.rockPaperScissors())
