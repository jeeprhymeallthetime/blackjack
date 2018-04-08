#Actions for Blackjack

def deal_card(given_deck):
    select_card = given_deck[0]
    given_deck.pop(0)
    return select_card, given_deck


def score_hand(hand):
    points = 0
    for i in range(0, len(hand)):
        if hand[i].value == 1:
            hand[i].ace_boost = True
        points += hand[i].points

    if points > 21:
        aces_high = True
        ace_in_hand = []
        #ace_count = len(ace_in_hand)
        ace_try = 0
        while aces_high is True:
            ace_count = len(ace_in_hand)
            ace_in_hand = []
            ace_looper = 0

            for i in range(0, len(hand)):
                if hand[i].value == 1:
                    ace_in_hand.append(True)
                    ++ace_looper
                if ace_looper > ace_count:
                    break
            ace_count = len(ace_in_hand)
            ace_looper = 0
            if any(check is True for check in ace_in_hand):
                points = 0
                for i in range(0, len(hand)):
                    if hand[i].value == 1 and ace_looper < ace_count:
                        hand[i].ace_boost = False
                        ++ace_looper
                    points += hand[i].points
                    ++ace_try
            if points < 22 or ace_try == len(hand):
                aces_high = False


    #for i in range(0, len(hand)):
    #    points += hand[i].points

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
    dealer_hand[0].ace_boost = True
    dealer_hand[1].ace_boost = True
    dealer_hand[0].ace_ask = True
    dealer_hand[1].ace_ask = True

    return player_hand, dealer_hand, shuffled_deck

def run_turn(turns_hand, active_deck):
    end_turn = False
    while end_turn == False:
        choice = 'n'
        while choice != 'S' and choice != 's' and choice != 'H' and choice != 'h':
            choice = input("How would you like to proceed? Hit (H) or Stay(S)?")
            if choice == 'H' or choice == 'h':
                dealt_card, active_deck = deal_card(active_deck)
                print("You received: ",dealt_card)
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

    return score_hand(turns_hand), active_deck