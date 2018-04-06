#from random import *

#print(random())

suits = ['spades','hearts','clubs', 'diamonds']
values = range(1,13)

#Defining a class called "Card" which should have the properties
#of a basic card from a deck of 52.


class OldCard:
    def __init__(self):
        self.suit = "spades"
        self.value = 1
        self.face = False

    def face_search(self):
        if self.value in range(10, 13):
            self.face = True
        else:
            self.face = False

    def move_up(self):
        self.value += 1


class Card:
    def __init__(self):
        self.suit = "spades"
        self.value = 1

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, val):
        self._value = val
        if self._value in range(10, 13):
            self._face = True
        else:
            self._face = False

    @property
    def face(self):
        return self._face

    def move_up(self):
        self.value += 1



deck = []
for i in range(0,52):
    new_card = card()
    deck.append(new_card)


#def function(self):
#    print("This is a message inside the class.")
