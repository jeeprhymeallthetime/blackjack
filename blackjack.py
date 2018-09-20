from cards import deck
from actions import act_funcs
from actions import game
from actions import players
from actions import quiet_output
import numpy as np
import time
wallet = 100
col = []
start = time.time()
for i in range(0,300):
    d = deck.Deck(number = 6)
    d.shuffle_deck()
    p = players.Player()
    p._position = "vifsitor"
    shuffled_deck = d.cards
    #with quiet_output.suppress_stdout():
    shuffled_deck, wallet, wins, total = game.play_game(shuffled_deck, wallet, p)
    #print("Total wins = ",wins," and Total games = ", total)
    #print("Win Rate = ",wins/total)
    col.append(wins/total)
print("Average win rate = ", np.mean(col))
print("Standard Deviation = ", np.std(col))
end = time.time()
print("Time elapsed = ", end - start, " seconds")