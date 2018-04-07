class Card:
    def __init__(self, suit="spades", value=1):
        self._suit = suit
        self._value = value
        self._ace_boost = False
        self._points = value
        self._face = False

    def __str__(self):
        return '%s of %s which has a point value of %s and its face status is %s'\
               % (self.value, self.suit, self.points, self.face)

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

    @property
    def face(self):
        return self._face



    # This is a relic of examples I found online.  Helpful for POC work

    def move_up(self):
        self.value += 1
