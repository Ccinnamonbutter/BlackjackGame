from player import Player
from dealer import Dealer
from game import Game

STARTING_BALANCE = 500
player = Player(STARTING_BALANCE)
dealer = Dealer()
game = Game(player, dealer)

game.start_game()

print("Welcome to Blackjack!")
x=(input('you are starting with $500.would you play a hand? ' ))
while True:
    bets= (input ('Place your bet: '))
    if int(bets ) < 0 :
               print ("The minimum bet is $1. ")
    elif (int(bets) > int(STARTING_BALANCE)):
            print("Insufficient balance. Your balance is $500.")
    else:
        break

def balance_counter (bets):
    bet_counter= int(bets - STARTING_BALANCE)

    print (bet_counter)