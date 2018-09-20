from actions import act_funcs

def split_hand(player_hand, shuffled_deck):
    hand_one, hand_two = player_hand[0], player_hand[1]
    dealt_card, shuffled_deck = act_funcs.deal_card(shuffled_deck)
    hand_one.append(dealt_card)
    dealt_card, shuffled_deck = act_funcs.deal_card(shuffled_deck)
    hand_two.append(dealt_card)
    if hand_one[0] == hand_one[1]:
        split_1 = input("An opportunity to split again.  Do you take it?(Y/N)")
        if split_1 == "Y":
            hand_one, hand_three = hand_one[0], hand_one[1]
            scenario_1 = True
        else:
            scenario_1 = False
            hand_three = 0
    if hand_two[0] == hand_two[1]:
        split_2 = input("An opportunity to split again.  Do you take it?(Y/N)")
        if split_2 == "Y":
            hand_two, hand_four = hand_two[0], hand_two[1]
            scenario_2 = True
        else:
            scenario_2 = False
            hand_four = 0
    if scenario_1 == False and scenario_2 == False:
        return hand_one, hand_two, hand_three, hand_four, shuffled_deck, 1, 2
    if scenario_1 == True and scenario_2 == False:
        return hand_one, hand_two, hand_three, hand_four, shuffled_deck, 2, 3
    if scenario_1 == False and scenario_2 == True:
        return hand_one, hand_two, hand_three, hand_four, shuffled_deck, 3, 3
    if scenario_1 == True and scenario_2 == True:
        return hand_one, hand_two, hand_three, hand_four, shuffled_deck, 4, 4


def split_play(hand_one, hand_two, hand_three, hand_four, shuffled_deck, scenario_num, num_hands, dealer_hand):
    busted_one = False
    busted_two = False
    busted_three = False
    busted_four = False
    busted = False
    if scenario_num == 1:
        shuffled_deck, busted_one, hand_one = act_funcs.run_player_turn(hand_one, dealer_hand, shuffled_deck)
        shuffled_deck, busted_two, hand_two = act_funcs.run_player_turn(hand_two, dealer_hand, shuffled_deck)
    if scenario_num == 2:
        shuffled_deck, busted_one, hand_one = act_funcs.run_player_turn(hand_one, dealer_hand, shuffled_deck)
        shuffled_deck, busted_two, hand_two = act_funcs.run_player_turn(hand_two, dealer_hand, shuffled_deck)
        shuffled_deck, busted_three, hand_three = act_funcs.run_player_turn(hand_three, dealer_hand, shuffled_deck)
    if scenario_num == 3:
        shuffled_deck, busted_one, hand_one = act_funcs.run_player_turn(hand_one, dealer_hand, shuffled_deck)
        shuffled_deck, busted_two, hand_two = act_funcs.run_player_turn(hand_two, dealer_hand, shuffled_deck)
        shuffled_deck, busted_four, hand_four = act_funcs.run_player_turn(hand_four, dealer_hand, shuffled_deck)
    if scenario_num == 4:
        shuffled_deck, busted_one, hand_one = act_funcs.run_player_turn(hand_one, dealer_hand, shuffled_deck)
        shuffled_deck, busted_two, hand_two = act_funcs.run_player_turn(hand_two, dealer_hand, shuffled_deck)
        shuffled_deck, busted_three, hand_three = act_funcs.run_player_turn(hand_three, dealer_hand, shuffled_deck)
        shuffled_deck, busted_four, hand_four = act_funcs.run_player_turn(hand_four, dealer_hand, shuffled_deck)
    if busted_one == False or busted_two == False or busted_three == False or busted_four == False:
        busted = False
    if busted_one == True and busted_two == True and busted_three == True and busted_four == True:
        busted = True
    return shuffled_deck, busted, busted_one, busted_two, busted_three, busted_four, hand_one, hand_two, hand_three, hand_four


def start_of_hand(player_hand, dealer_hand, shuffled_deck, bet, p):
    busted = False
    split = "N"
    scenario_num = 0
    busted_one = False
    busted_two = False
    busted_three = False
    busted_four = False
    if act_funcs.dealer_win_check(dealer_hand) is True:
        print("Dealer has Blackjack! Everybody loses.")
        print("Their cards were:", dealer_hand[0], "and", dealer_hand[1])
    else:
        print("Dealer holds a hidden card and a", dealer_hand[1])
        print("Your cards are:")
        print(player_hand[0], " : ", player_hand[1])
        print("You have", act_funcs.score_hand(player_hand), "points")
        if player_hand[0].value == player_hand[1].value:
            split = input("Would you like to split? (Y/N)")
            if split == "Y":
                hand_one, hand_two, hand_three, hand_four, shuffled_deck, scenario_num, num_hands = \
                    split_hand(player_hand, shuffled_deck)
                shuffled_deck, busted, busted_one, busted_two, busted_three, busted_four, \
                hand_one, hand_two, hand_three, hand_four = split_play(hand_one, hand_two, \
                hand_three, hand_four, shuffled_deck, scenario_num, num_hands, dealer_hand)
        else:
            shuffled_deck, busted, player_hand = act_funcs.run_player_turn(player_hand, dealer_hand, shuffled_deck)
        #shuffled_deck, busted, player_hand = act_funcs.run_player_turn(player_hand, dealer_hand, shuffled_deck, p)
    return shuffled_deck, busted, split, scenario_num, busted_one, busted_two, busted_three, busted_four


def end_of_hand(busted, player_hand, dealer_hand, shuffled_deck, bet):
    if busted is False:
        dealer_hand, shuffled_deck = act_funcs.dealers_turn(dealer_hand, shuffled_deck)
        if act_funcs.score_hand(dealer_hand) > 21:
            print("Dealer busts! Everybody wins")
            result = 0
        elif act_funcs.score_hand(player_hand) > act_funcs.score_hand(dealer_hand):
            print("Player wins!")
            result = 1
        elif act_funcs.score_hand(dealer_hand) == act_funcs.score_hand(player_hand):
            print("Push")
            result = 1
        else:
            print("Player loses.")
            result = 0
        print("Final score:")
        hand_print = ''
        for i in range(0,len(dealer_hand)):
            hand_print += str(dealer_hand[i].value) + ' of ' + dealer_hand[i].suit + ', '
        print("Dealer Hand:", hand_print[:-2], '- Final Score: ', act_funcs.score_hand(dealer_hand))
        hand_print = ''
        for i in range(0, len(player_hand)):
            hand_print += str(player_hand[i].value) + ' of ' + player_hand[i].suit + ', '
        print("Player Hand:", hand_print[:-2], '- Final Score: ', act_funcs.score_hand(player_hand))
    else:
        result = 0
    return result


def end_of_hand_split(busted, player_hand, dealer_hand, shuffled_deck, bet, scenario_num):
    if busted is False:
        dealer_hand, shuffled_deck = act_funcs.dealers_turn(dealer_hand, shuffled_deck)
        if act_funcs.score_hand(dealer_hand) > 21:
            print("Dealer busts! Everybody wins")
            result = 0
        elif act_funcs.score_hand(player_hand) > act_funcs.score_hand(dealer_hand):
            print("Player wins!")
            result = 1
        elif act_funcs.score_hand(dealer_hand) == act_funcs.score_hand(player_hand):
            print("Push")
            result = 1
        else:
            print("Player loses.")
            result = 0
        print("Final score:")
        hand_print = ''
        for i in range(0,len(dealer_hand)):
            hand_print += str(dealer_hand[i].value) + ' of ' + dealer_hand[i].suit + ', '
        print("Dealer Hand:", hand_print[:-2], '- Final Score: ', act_funcs.score_hand(dealer_hand))
        hand_print = ''
        for i in range(0, len(player_hand)):
            hand_print += str(player_hand[i].value) + ' of ' + player_hand[i].suit + ', '
        print("Player Hand:", hand_print[:-2], '- Final Score: ', act_funcs.score_hand(player_hand))
    else:
        result = 0
    return result


def play_game(shuffled_deck, wallet, p):
    game_on = True
    h_line = ""
    for i in range(50):
        h_line += '-'
    wins = 0
    total = 0
    while game_on is True:
        print(h_line)
        #bet = input("How much would you like to bet this hand?")
        bet = 12
        scenario_num = 0
        dealer_hand, player_hand, shuffled_deck = act_funcs.first_deal(shuffled_deck)
        shuffled_deck, busted, split, scenario_num = start_of_hand(player_hand, dealer_hand, shuffled_deck, bet, p)

        if scenario_num == 0:
            result = end_of_hand(busted, player_hand, dealer_hand, shuffled_deck, bet)
        else:
            result = end_of_hand_split(busted, player_hand, dealer_hand, shuffled_deck, bet, scenario_num)
        wins = wins + result
        total = total + 1
        print(total)
        choice = input("Another hand?")
        #choice = 'Y'
        #if total < 100:
        #    choice = 'Y'
        #else:
        #    choice = 'N'
        if choice not in ('Yes', 'yes', 'y', 'Y', 'sure', 'Sure', 'yup'):
            game_on = False

    return shuffled_deck, wallet, wins, total
