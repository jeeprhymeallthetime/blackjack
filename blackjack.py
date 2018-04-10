from cards import deck
from actions import act_funcs

shuffled_deck = deck.FiftyTwo.generate_deck()

#while(keep_playing = True):

dealer_hand, player_hand, shuffled_deck = act_funcs.first_deal(shuffled_deck)
dealer_points = act_funcs.score_hand(dealer_hand)
#print(dealer_hand[0],dealer_hand[1])
#print(dealer_points)



print("Dealer holds a hidden card and a",dealer_hand[1])
print("Your cards are:")
print(player_hand[0], " : ", player_hand[1])
print("You have", act_funcs.score_hand(player_hand), "points")

player_points, shuffled_deck = act_funcs.run_player_turn(player_hand, shuffled_deck)


#Test
