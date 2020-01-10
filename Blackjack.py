from Deck import Deck
from Player import Player
from Round import Round

deck = Deck(1)

Dealer = Player("Dealer", True)
Nate = Player("Nate")
Katherine = Player("Katherine")
Seth = Player("Seth")

Players = [Dealer, Nate, Katherine, Seth]

for player in Players:
    player.bank = 1000

numRounds = 5
currentRound = 0

while currentRound < numRounds:
    newRound = Round(Players, deck)
    newRound.play_out_round()
    currentRound += 1