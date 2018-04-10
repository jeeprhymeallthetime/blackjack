from cards import deck
from actions import act_funcs
from actions import game

shuffled_deck = deck.FiftyTwo.generate_deck()

#while(keep_playing = True):

dealer_hand, player_hand, shuffled_deck = act_funcs.first_deal(shuffled_deck)
dealer_points = act_funcs.score_hand(dealer_hand)
print(dealer_hand[0],dealer_hand[1])
#print(dealer_points)

dealer_hand, player_hand, shuffled_deck = game.play_game(dealer_hand, player_hand, shuffled_deck)