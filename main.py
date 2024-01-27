from player import Player
from dealer import Dealer
from game import Game

STARTING_BALANCE = 500
player = Player(STARTING_BALANCE)
dealer = Dealer()
game = Game(player, dealer)

game.start_game()

print("Welcome to Blackjack!")
print()
game.start_game()