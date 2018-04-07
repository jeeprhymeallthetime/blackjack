#Defining a class called "Card" which should have the properties
#of a basic card from a deck of 52.

class Card:
    def __init__(self):
        self.suit = "spades"
        self.value = 1

    @property
    def value(self):
        return self._value

    # This takes in new values input during the deck building
    # and changes a note on whether or not it's a face card

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

    # This is a relic of examples I found online.  Helpful for POC work

    def move_up(self):
        self.value += 1

    def print(self):
        print("Suit = ",self.suit, " Card Value = ", self.value)

suits = ['spades','hearts','clubs', 'diamonds']
values = range(1,14)



placeholder_deck = []
for i in suits:
    for j in values:
        placeholder_deck.append([i,j])
from random import *
placeholder_deck[randint(0,51)]


deck = []
for i in range(0, 52):
    new_card = Card()
    deck.append(new_card)

for i in range(0,51):
    card = randint(0, len(placeholder_deck) - 1)
    pick_a_card = placeholder_deck[card]
    placeholder_deck.pop(card)
    deck[i].suit = pick_a_card[0]
    deck[i].value = pick_a_card[1]






#####The following is deprecated or experimental code use in the development of this work
t = []
for i in range(0,1048528):
    t.append(randint(0,51))

import csv

with open('t_cell_count.csv', 'w', newline='') as myfile:
    wr = csv.writer(myfile, delimiter=',',)
    for i in t:
        wr.writerow([i])

#def function(self):
#    print("This is a message inside the class.")
