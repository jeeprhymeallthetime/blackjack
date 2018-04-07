class Card:
    def __init__(self, suit="spades", value=1):
        self.suit = suit
        self.value = value

    def __str__(self):
        return '%s of %s' % (self.value, self.suit)

    @property
    def value(self):
        return self._value

    # This takes in new values input during the deck building
    # and changes a note on whether or not it's a face card

    @value.setter
    def value(self, val):
        self._value = val
        if self._value in range(10, 14):
            self._face = True
        else:
            self._face = False

    @property
    def face(self):
        return self._face

    @property
    def value(self):
        return self._value

    # This takes in new values input during the deck building
    # and changes a note on whether or not it's a face card

    @value.setter
    def value(self, val):
        self._value = val
        print(val)
        if self._value in range(10, 14):
            self._points = 10
        else:
            self._points = val

    @property
    def points(self):
        return self._points

    # This is a relic of examples I found online.  Helpful for POC work

    def move_up(self):
        self.value += 1

    def print(self):
        print(self.value,"of",self.suit)