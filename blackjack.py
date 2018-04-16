from cards import deck
from actions import act_funcs
from actions import game
wallet = 100
d = deck.Deck()
d.shuffle_deck()
shuffled_deck = d.cards
shuffled_deck, wallet = game.play_game(shuffled_deck, wallet)