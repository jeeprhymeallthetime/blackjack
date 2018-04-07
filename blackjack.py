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

print("Dealer holds a hidden card and a",dealer_hand[0])
print("Your cards are:")
print(player_hand[0]," : ",player_hand[1])
print(player_hand[0].points)
for i in range(0,len(player_hand)):
    if player_hand[i].value == 1:
        choice = input("You have an Ace.  Do you want that worth 1 or 11?")



