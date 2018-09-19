from cards import deck
from actions import act_funcs
from actions import game
from actions import players
from actions import quiet_output
wallet = 100
d = deck.Deck(number = 6)
d.shuffle_deck()
p = players.Player()
shuffled_deck = d.cards
with quiet_output.suppress_stdout():
    shuffled_deck, wallet, wins, total = game.play_game(shuffled_deck, wallet, p)
print("Total wins = ",wins," and Total games = ", total)
print("Win Rate = ",wins/total)
