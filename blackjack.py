from cards import deck
from actions import act_funcs
from actions import game

shuffled_deck = deck.FiftyTwo.generate_deck()
dealer_hand, player_hand, shuffled_deck = game.play_game(shuffled_deck)