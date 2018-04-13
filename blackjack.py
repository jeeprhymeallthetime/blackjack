from cards import deck
from actions import act_funcs
from actions import game
wallet = 100
shuffled_deck = deck.FiftyTwo.generate_deck()
shuffled_deck, wallet = game.play_game(shuffled_deck, wallet)