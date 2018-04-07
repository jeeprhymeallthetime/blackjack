#Actions for Blackjack

def deal_card(given_deck):
    select_card = given_deck[0]
    given_deck.pop(0)
    return select_card, given_deck


def score_hand(hand):
    for i in range(0, len(hand)):
        choice = 0
        if hand[i].value == 1 and hand[i].ace_ask is False:
            hand[i].ace_ask = True
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

def run_turn(turns_hand, active_deck):
    end_turn = False
    while end_turn == False:
        choice = 'n'
        while choice != 'S' and choice != 's' and choice != 'H' and choice != 'h':
            choice = input("How would you like to proceed? Hit (H) or Stay(S)?")
            if choice == 'H' or choice == 'h':
                dealt_card, active_deck = deal_card(active_deck)
                turns_hand.append(dealt_card)
                print("You have", score_hand(turns_hand), "points")
            elif choice == 'S' or choice == 's':
                end_turn = True
                pass
            else:
                print("That is an invalid entry, please try again")

        if score_hand(turns_hand) > 21:
            print("You bust!")
            end_turn = True

    return active_deck