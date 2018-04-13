#Actions for Blackjack

def deal_card(given_deck):
    select_card = given_deck[0]
    given_deck.pop(0)
    return select_card, given_deck

#The following sums the number of points in the hand
#There is conditional pieces that change the number of points for an Ace
#Depending on if the "points" sum busts over 21 points
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
        #ace_try = 0
        #Prepare total number of aces in hand in case we check them all to 1 and the hand is still a bust
        total_aces = 0
        for i in range(0, len(hand)):
            if hand[i].value == 1:############## Right here
                total_aces += 1
        #Beginning the investigation into the impact of Aces on the points of the hand
        #Go through one Ace at a time and evaluate the number of points
        #If changing 1 Ace doesn't work, try another
        #If there are no more Aces, total the number of points and return
        while aces_high is True:
            ace_count = len(ace_in_hand)
            ace_in_hand = []
            ace_looper = 0
            #Check to find an Ace - stop after the new 'new' Ace discovery in the hand
            for i in range(0, len(hand)):
                if hand[i].value == 1:
                    ace_in_hand.append(True)
                    ace_looper += 1
                if ace_looper > ace_count:
                    break
            ace_count = len(ace_in_hand)
            ace_looper = 0
            #The If statement may be redundant -
            #it was written for when I thought we'd go through each card
            #rather than just the Aces.  Either way:
            #The code here reduces the Ace_Boost to False, bringing the points value down to 1
            #Then recalculates the points in the hand
            if any(check is True for check in ace_in_hand):
                points = 0
                for i in range(0, len(hand)):
                    if hand[i].value == 1 and ace_looper < ace_count:
                        hand[i].ace_boost = False
                        ace_looper += 1
                    points += hand[i].points
                    #ace_try += 1
            #If reducing the Ace didn't successfully reduce the number of points below a bust
            #Iterate again for new Aces.
            #If there are no more Aces the move on with a total of points
            if points < 22 or ace_count == total_aces:
                aces_high = False
    return points

def first_deal(shuffled_deck):
    dealer_hand = []
    player_hand = []
    #Selecting a card from a shuffled deck of 52 cards and distribute in a clockwise fashion with dealer last
    dealt_card, shuffled_deck = deal_card(shuffled_deck)
    player_hand.append(dealt_card)
    dealt_card, shuffled_deck = deal_card(shuffled_deck)
    dealer_hand.append(dealt_card)
    dealt_card, shuffled_deck = deal_card(shuffled_deck)
    player_hand.append(dealt_card)
    dealt_card, shuffled_deck = deal_card(shuffled_deck)
    dealer_hand.append(dealt_card)
    dealer_hand[0].ace_boost = True
    dealer_hand[1].ace_boost = True
    dealer_hand[0].ace_ask = True
    dealer_hand[1].ace_ask = True

    return player_hand, dealer_hand, shuffled_deck

#Check to see if the dealer has blackjack right off the bat
def dealer_win_check(hand):
    d_points = score_hand(hand)
    if d_points == 21:
        dealer_wins=True
    else:
        dealer_wins=False
    return dealer_wins

def ace_check(hand):
    ace_boosted = False
    for i in range(0,len(hand)):
        if hand[i].ace_boost == True:
            ace_boosted = True
    return ace_boosted

#Dealer plays last, hits on 16 or below
def dealers_turn(hand, active_deck):
    while score_hand(hand) < 17 or (score_hand(hand) == 17 and ace_check(hand) is True):
        dealt_card, active_deck = deal_card(active_deck)
        print("Dealer receives: ",dealt_card)
        hand.append(dealt_card)

    return hand, active_deck

#This function governs the player's turns.
#The player is allowed to Hit or Stand
#A Hit will give them a card, a Stand will cease their turn
#If the player passes 21 points after any hit, they lose
def run_player_turn(turns_hand, active_deck):
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
            busted = True
        else:
            busted = False

    return active_deck, busted, turns_hand