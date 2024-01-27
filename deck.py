import random
from card import Card
class Deck:
    def __init__(self,cards):
         self.cards = []    
         self.create_deck()
         self.shuffle()   

    def create_deck(self):
        for suit in range(4):  # There are 4 suits
            for rank in range(1, 14):  # Ranks from 1 to 13
                self.cards.append(Card(suit, rank))


    def shuffle(self):
         random.choice(self.cards)
         
         
    def deal(self,n):
        cards_dealt=[]
        for x in range (n):
            #will treat the end of the list as the top of the deck
            
            top_card= self.cards.pop()
            cards_dealt.append(top_card)
            return cards_dealt
    
    
