from cards import deck
from actions import deal

shuffled_deck = deck.FiftyTwo.generate_deck()

dealer_hand = []
player_hand = []


dealt_card, shuffled_deck = deal.deal_card(shuffled_deck)
dealer_hand.append(dealt_card)
dealt_card, shuffled_deck = deal.deal_card(shuffled_deck)
player_hand.append(dealt_card)
dealt_card, shuffled_deck = deal.deal_card(shuffled_deck)
dealer_hand.append(dealt_card)
dealt_card, shuffled_deck = deal.deal_card(shuffled_deck)
player_hand.append(dealt_card)

print(dealer_hand[0])
print(dealer_hand[1])
print(player_hand[0])
print(player_hand[1])





