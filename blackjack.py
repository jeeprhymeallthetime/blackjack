from cards import deck
from actions import act_funcs
from actions import game_auto
from actions import players
from actions import quiet_output
import numpy as np
import time
wallet = 1000
wallet_track = []
col = []
start = time.time()
for i in range(0,10):
    d = deck.Deck(number = 6)
    d.shuffle_deck()
    p = players.Player()
    p._position = "vifsitor"
    shuffled_deck = d.cards
    #with quiet_output.suppress_stdout():
    shuffled_deck, wallet, wins, total, wallet_track = game_auto.play_game(shuffled_deck, wallet, p, wallet_track)
    #print("Total wins = ",wins," and Total games = ", total)
    #print("Win Rate = ",wins/total)
    col.append(wins/total)
print("Average win rate = ", np.mean(col))
print("Standard Deviation = ", np.std(col))
end = time.time()
print("Time elapsed = ", end - start, " seconds")