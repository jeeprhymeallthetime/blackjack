#Actions for Blackjack

def deal_card(given_deck):
    select_card = given_deck[0]
    given_deck.pop(0)
    return select_card, given_deck

def score_hand(hand):
    for i in range(0, len(hand)):
        choice = 0
        if hand[i].value == 1:
            while choice != 1 and choice != 11:
                choice = int(input("You have an Ace.  Do you want that worth 1 or 11?"))
                if (choice == 1 or choice == 11):
                    print("You have selected ", choice)
                    if choice == 11:
                        hand[i].ace_boost = True
                    else:
                        hand[i].ace_boost = False
                else:
                    print("You have made an invalid selection.  Please try again")

    points = 0

    for i in range(0, len(hand)):
        points += hand[i].points

    return points

def first_deal(shuffled_deck):
    dealer_hand = []
    player_hand = []
    dealt_card, shuffled_deck = deal_card(shuffled_deck)
    dealer_hand.append(dealt_card)
    dealt_card, shuffled_deck = deal_card(shuffled_deck)
    player_hand.append(dealt_card)
    dealt_card, shuffled_deck = deal_card(shuffled_deck)
    dealer_hand.append(dealt_card)
    dealt_card, shuffled_deck = deal_card(shuffled_deck)
    player_hand.append(dealt_card)

    return player_hand, dealer_hand, shuffled_deck
