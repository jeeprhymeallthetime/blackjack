from random import *
from cards import card


class Deck:

    def __init__(self, number = 1, suits = ['Spades', 'Hearts', 'Clubs', 'Diamonds'], values = range(1,14)):
        self._number = number
        self._suits = suits
        self._values = values
        self._cards = []
        for k in range(1,self._number+1):
            for i in self._suits:
                for j in self._values:
                    self._cards.append(card.Card(suit = i, value = j))


    @property
    def number(self):
        return self._number

    @property
    def suits(self):
        return self._suits

    @property
    def values(self):
        return self._values

    @property
    def cards(self):
        return self._cards

    def shuffle_deck(self):
        for i in range(1,1000):
                shuffle(self._cards)

