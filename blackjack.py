from cards import deck
from actions import deal

shuffled_deck = deck.FiftyTwo.generate_deck()

dealer_hand = []
player_hand = []

#This is just a test for PyCharm Commits
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

# for i in range(0,len(player_hand)):
#     choice = 0
#     if player_hand[i].value == 1:
#         while(choice != 1 or choice != 11):
#             choice = input("You have an Ace.  Do you want that worth 1 or 11?")
#             if (choice == 1 or choice == 11):
#                 print("You have selected ",choice)
#             else:
#                 print("You have made an invalid selection.  Please try again")
#     else:
#         choice = player_hand[i].points
#     player_hand[i].points = choice

print("You have ",player_hand[0].points + player_hand[1].points," points")
