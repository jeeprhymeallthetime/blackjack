from actions import act_funcs
class Player:
    def __init__(self, position = "visitor"):
        self._position = position
        self._player_hand = []

    @property
    def type(self):
        return self._type

    def __str__(self):
        #Return the cards in a player's hand
#        if self._position == "visitor":
        hand_print = ''
        for i in range(0, len(self._player_hand)):
            hand_print += str(self._player_hand[i].value) + ' of ' + self._player_hand[i].suit + ', '
        print("Player Hand:", hand_print[:-2], '- Score: ', act_funcs.score_hand(self._player_hand))

