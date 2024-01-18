import random
from card import Card
class Deck:
    def __init__(self,cards):
         self.cards = []       

    def create_deck(self):
        for suit in range(4):  # There are 4 suits
            for rank in range(1, 14):  # Ranks from 1 to 13
                self.cards.append(Card(suit, rank))


    def shuffle(self):
         random.choice(self.cards)
         
         
    def deal(n):
        cards_dealt=[]
        for x in range (n):
            card= card.pop()
            cards_dealt.append(card)
            return cards_dealt
        
    
