import random

class Cards:

    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def show(self):
        print("{} of {}".format(self.value, self.suit))


class Deck:
    def __init__(self):
        self.cards = []
        self.build()

    def show(self):
        for c in self.cards:
            c.show()

    def build(self):
        suits = ["Clubs", "Hearts", "Spades", "Diamonds"]
        values = ["2","3","4","5","6","7","8","9","Jack","Queen","King","Ace"]
        for suit in suits:
            for value in values:
                self.cards.append(Cards(suit,value))

    def shuffle(self):
        return random.shuffle(self.cards)

    def drawCards(self):
        count = 1
        lst = []
        while(count != 5):
            return self.cards.pop()
            count = count + 1



class Player:
    def __init__(self,name):
        self.hand = []
        self.name = name


    def draw(self, deck):
        self.hand.append(deck.drawCards())
        return self

    def showHand(self):
        for c in self.hand:
            c.show()

deck = Deck()
deck.shuffle()
"""
deck.show()
"""

me = Player("pl")
me.draw(deck)
me.showHand()









