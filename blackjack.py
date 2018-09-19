from cards import deck
from actions import act_funcs
from actions import game
from actions import players
wallet = 100
d = deck.Deck(number = 6)
d.shuffle_deck()
p = players.Player()
shuffled_deck = d.cards
shuffled_deck, wallet = game.play_game(shuffled_deck, wallet, p)