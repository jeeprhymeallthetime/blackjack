class Card:
    def __init__(self, suit="spades", value=1, ace_boost=False):
        self._suit = suit
        self._value = value
        self._ace_boost = ace_boost

    def __str__(self):
        return '%s of %s' % (self.value, self.suit)

    @property
    def value(self):
        return self._value


    # This takes in new values input during the deck building
    # and changes a note on whether or not it's a face card
    @property
    def ace_boost(self):
        return self._ace_boost

    @value.setter
    def value(self, val):
        self._value = val
        if (self._value in range(10, 14)):
            self._face = True
            self._points = 10
        else:
            self._face = False
            self._points = val

    @ace_boost.setter
    def ace_boost(self, val):
        self._ace_boost = val

    @property
    def face(self):
        return self._face

    @property
    def points(self):
        return self._points


    # This is a relic of examples I found online.  Helpful for POC work

    def move_up(self):
        self.value += 1
