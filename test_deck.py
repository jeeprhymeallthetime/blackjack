from cards import card
from actions import players
from actions import game
test_deck = [card.Card(value = 2, suit = 'spade'), card.Card(value = 2, suit = 'heart'), card.Card(value = 2, suit = 'club'), card.Card(value = 2, suit = 'diamond'), card.Card(value = 2, suit = 'soul'), card.Card(value = 2, suit = 'knot'), card.Card(value = 2, suit = 'spade'), card.Card(value = 2, suit = 'heart'), card.Card(value = 2, suit = 'club'), card.Card(value = 2, suit = 'diamond'), card.Card(value = 2, suit = 'soul'), card.Card(value = 2, suit = 'knot'), card.Card(value = 2, suit = 'spade'), card.Card(value = 2, suit = 'heart'), card.Card(value = 2, suit = 'club'), card.Card(value = 2, suit = 'diamond'), card.Card(value = 2, suit = 'soul'), card.Card(value = 2, suit = 'knot')]
wins = 0
wallet = 0
total = 0
p = players.Player()
test_deck, wallet, wins, total, game.play_game(test_deck, wallet, p)