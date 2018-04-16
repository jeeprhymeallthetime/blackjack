#This code defines the "Card" class for the blackjack code
#Every class will have 6 attributes
#  suit - Suit of the card that it belongs to.  Examples, Clubs, Hearts, Spades, Diamonds
#  value - The number value of the card
#  points - This is currently tied to the point values for blackjack and is not generalized beyond that
#  ace_boost - Also tied to blackjack like the 'points' attribute is -
#              flips the point for value = 1 from 1 to 11 if True
#  ace_ask - Possibly deprecated; past versions of the blackjack code asked the user
#            which points amount they wanted for an ace
#  face - An indicator of if the value of the card represents a "face" value of a typical 52 card deck


class Card:
    def __init__(self, suit="spades", value=1):
        self._suit = suit
        self._value = value
        self._ace_boost = False
        self._ace_ask = False
        self._face = False
        if self._value in range(10, 14):
            self._face = True
            self._points = 10
        else:
            self._face = False
            self._points = self._value

    def __str__(self):
        #return '%s of %s which has a point value of %s and its face status is %s'\
        #       % (self.value, self.suit, self.points, self.face)
        return '%s of %s'\
              % (self.value, self.suit)


    @property
    def value(self):
        return self._value

    @property
    def ace_boost(self):
        return self._ace_boost

    @property
    def points(self):
        return self._points

    @property
    def suit(self):
        return self._suit

    @property
    def ace_ask(self):
        return self._ace_ask

    # This takes in new values input during the deck building
    # and changes a note on whether or not it's a face card
    @value.setter
    def value(self, val):
        self._value = val
        if (self._value in range(10, 14)):
            self._face = True
            self._points = 10
        else:
            self._face = False
            self._points = val
        #If for some reason the value of the card changes and ace boost is turned on
        #The boosted points value remains
        if self._ace_boost == True and self._value == 1:
            self._points = 11


    #When the user is give the option to make an Ace worth 11 or 1,
    ## this will update the points attribute
    @ace_boost.setter
    def ace_boost(self, val):
        self._ace_boost = val
        if self._ace_boost == True and self._value == 1:
            self._points = 11
        elif self._ace_boost == False and self._value == 1:
            self._points = 1

    @ace_ask.setter
    def ace_ask(self, val):
        self._ace_ask = val

    @suit.setter
    def suit(self, val):
        self._suit = val

    @property
    def face(self):
        return self._face



    # This is a relic of examples I found online.  Helpful for POC work

    def move_up(self):
        self.value += 1
