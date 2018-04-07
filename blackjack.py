from cards import deck
from actions import act_funcs

shuffled_deck = deck.FiftyTwo.generate_deck()

dealer_hand, player_hand, shuffled_deck = act_funcs.first_deal(shuffled_deck)

print("Dealer holds a hidden card and a",dealer_hand[1])
print("Your cards are:")
print(player_hand[0], " : ", player_hand[1])
print("You have", act_funcs.score_hand(player_hand), "points")

shuffled_deck = act_funcs.run_turn(player_hand, shuffled_deck)





