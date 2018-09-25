from actions import act_funcs


def split_hand(player_hand, shuffled_deck):
    hand_one, hand_two, hand_three, hand_four = [], [], [], []
    hand_one.append(player_hand[0])
    hand_two.append(player_hand[1])
    dealt_card, shuffled_deck = act_funcs.deal_card(shuffled_deck)
    hand_one.append(dealt_card)
    print("New Hand #1:")
    print(hand_one[0], " : ", hand_one[1])
    print("You have", act_funcs.score_hand(hand_one), "points")
    dealt_card, shuffled_deck = act_funcs.deal_card(shuffled_deck)
    hand_two.append(dealt_card)
    print("New Hand #2:")
    print(hand_two[0], " : ", hand_two[1])
    print("You have", act_funcs.score_hand(hand_two), "points")
    scenario_1 = False
    scenario_2 = False
    hand_three = []
    hand_four = []
    if hand_one[0].value == hand_one[1].value:
        split_1 = input("An opportunity to split again.  Do you take it?(Y/N)")
        if split_1 == "Y":
            hand_three.append(hand_one[1])
            dealt_card, shuffled_deck = act_funcs.deal_card(shuffled_deck)
            hand_three.append(dealt_card)
            print("New Hand #3:")
            print(hand_three[0], " : ", hand_three[1])
            print("You have", act_funcs.score_hand(hand_three), "points")
            hand_one = [hand_one[0]]
            dealt_card, shuffled_deck = act_funcs.deal_card(shuffled_deck)
            hand_one.append(dealt_card)
            print("New Hand #1:")
            print(hand_one[0], " : ", hand_one[1])
            print("You have", act_funcs.score_hand(hand_one), "points")
            scenario_1 = True
        else:
            scenario_1 = False
            hand_three = []
    if hand_two[0].value == hand_two[1].value:
        split_2 = input("An opportunity to split again.  Do you take it?(Y/N)")
        if split_2 == "Y":
            hand_four.append(hand_two[1])
            dealt_card, shuffled_deck = act_funcs.deal_card(shuffled_deck)
            hand_four.append(dealt_card)
            print("New Hand #4:")
            print(hand_four[0], " : ", hand_four[1])
            print("You have", act_funcs.score_hand(hand_four), "points")
            hand_two = [hand_two[0]]
            dealt_card, shuffled_deck = act_funcs.deal_card(shuffled_deck)
            hand_two.append(dealt_card)
            print("New Hand #2:")
            print(hand_two[0], " : ", hand_two[1])
            print("You have", act_funcs.score_hand(hand_two), "points")
            scenario_2 = True
        else:
            scenario_2 = False
            hand_four = []
    if scenario_1 == False and scenario_2 == False:
        return hand_one, hand_two, hand_three, hand_four, shuffled_deck, 1, 2
    if scenario_1 == True and scenario_2 == False:
        return hand_one, hand_two, hand_three, hand_four, shuffled_deck, 2, 3
    if scenario_1 == False and scenario_2 == True:
        return hand_one, hand_two, hand_three, hand_four, shuffled_deck, 3, 3
    if scenario_1 == True and scenario_2 == True:
        return hand_one, hand_two, hand_three, hand_four, shuffled_deck, 4, 4


def split_play(hand_one, hand_two, hand_three, hand_four, shuffled_deck, scenario_num, num_hands, dealer_hand, p):
    busted_one = False
    busted_two = False
    busted_three = False
    busted_four = False
    busted = False
    if scenario_num == 1:
        print("Split Scenario #1")
        print("Playing Hand #1")
        shuffled_deck, busted_one, hand_one = act_funcs.run_player_turn_auto(hand_one, dealer_hand, shuffled_deck, p)
        print("Playing Hand #2")
        shuffled_deck, busted_two, hand_two = act_funcs.run_player_turn_auto(hand_two, dealer_hand, shuffled_deck, p)
    if scenario_num == 2:
        print("Split Scenario #2")
        print("Playing Hand #1")
        shuffled_deck, busted_one, hand_one = act_funcs.run_player_turn_auto(hand_one, dealer_hand, shuffled_deck, p)
        print("Playing Hand #2")
        shuffled_deck, busted_two, hand_two = act_funcs.run_player_turn_auto(hand_two, dealer_hand, shuffled_deck, p)
        print("Playing Hand #3")
        shuffled_deck, busted_three, hand_three = act_funcs.run_player_turn_auto(hand_three, dealer_hand, shuffled_deck, p)
    if scenario_num == 3:
        print("Split Scenario #3")
        print("Playing Hand #1")
        shuffled_deck, busted_one, hand_one = act_funcs.run_player_turn_auto(hand_one, dealer_hand, shuffled_deck, p)
        print("Playing Hand #2")
        shuffled_deck, busted_two, hand_two = act_funcs.run_player_turn_auto(hand_two, dealer_hand, shuffled_deck, p)
        print("Playing Hand #4")
        shuffled_deck, busted_four, hand_four = act_funcs.run_player_turn_auto(hand_four, dealer_hand, shuffled_deck, p)
    if scenario_num == 4:
        print("Split Scenario #4")
        print("Playing Hand #1")
        shuffled_deck, busted_one, hand_one = act_funcs.run_player_turn_auto(hand_one, dealer_hand, shuffled_deck, p)
        print("Playing Hand #2")
        shuffled_deck, busted_two, hand_two = act_funcs.run_player_turn_auto(hand_two, dealer_hand, shuffled_deck, p)
        print("Playing Hand #3")
        shuffled_deck, busted_three, hand_three = act_funcs.run_player_turn_auto(hand_three, dealer_hand, shuffled_deck, p)
        print("Playing Hand #4")
        shuffled_deck, busted_four, hand_four = act_funcs.run_player_turn_auto(hand_four, dealer_hand, shuffled_deck, p)
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
    hand_one = []
    hand_two = []
    hand_three = []
    hand_four = []
    if act_funcs.dealer_win_check(dealer_hand) is True:
        print("Dealer has Blackjack! Everybody loses.")
        print("Their cards were:", dealer_hand[0], "and", dealer_hand[1])
    else:
        if player_hand[0].value == player_hand[1].value:
            print("Your cards are:")
            print(player_hand[0], " : ", player_hand[1])
            print("You have", act_funcs.score_hand(player_hand), "points")
            split = input("Would you like to split? (Y/N)")
            if split == "Y":
                hand_one, hand_two, hand_three, hand_four, shuffled_deck, scenario_num, num_hands = split_hand(
                    player_hand, shuffled_deck)
                shuffled_deck, busted, busted_one, busted_two, busted_three, busted_four, hand_one, hand_two, hand_three, hand_four = split_play(
                    hand_one, hand_two, hand_three, hand_four, shuffled_deck, scenario_num, num_hands, dealer_hand, p)
            else:
                shuffled_deck, busted, player_hand = act_funcs.run_player_turn_auto(player_hand, dealer_hand, shuffled_deck, p)
        else:
            shuffled_deck, busted, player_hand = act_funcs.run_player_turn_auto(player_hand, dealer_hand, shuffled_deck, p)
            # shuffled_deck, busted, player_hand = act_funcs.run_player_turn_auto(player_hand, dealer_hand, shuffled_deck, p)
    return shuffled_deck, busted, split, scenario_num, busted_one, busted_two, busted_three, busted_four, hand_one, hand_two, hand_three, hand_four


def end_of_hand(busted, player_hand, dealer_hand, bet, wallet):
    if busted is False:
        if act_funcs.score_hand(dealer_hand) > 21:
            print("Dealer busts! Everybody wins")
            result = 0
        elif act_funcs.score_hand(player_hand) > act_funcs.score_hand(dealer_hand):
            print("Player wins!")
            result = 1
        elif act_funcs.score_hand(dealer_hand) == act_funcs.score_hand(player_hand):
            print("Push")
            result = 1
            bet = 0
        else:
            print("Player loses.")
            result = 0
            bet = -1.0 * bet
        print("Final score:")
        hand_print = ''
        for i in range(0, len(dealer_hand)):
            hand_print += str(dealer_hand[i].value) + ' of ' + dealer_hand[i].suit + ', '
        print("Dealer Hand:", hand_print[:-2], '- Final Score: ', act_funcs.score_hand(dealer_hand))
        hand_print = ''
        for i in range(0, len(player_hand)):
            hand_print += str(player_hand[i].value) + ' of ' + player_hand[i].suit + ', '
        print("Player Hand:", hand_print[:-2], '- Final Score: ', act_funcs.score_hand(player_hand))
    else:
        result = 0
        print("You bust!")
        bet = bet * -1.0
    wallet = wallet + bet
    return result, wallet


def scen_1_split(dealer_hand, hand_one, hand_two, busted_one, busted_two, bet, wallet):
    print("Hand #1")
    result_1, wallet = end_of_hand(busted_one, hand_one, dealer_hand, bet, wallet)
    print("Hand #2")
    result_2, wallet = end_of_hand(busted_two, hand_two, dealer_hand, bet, wallet)
    return wallet, result_1, result_2


def scen_2_split(dealer_hand, hand_one, hand_two, hand_three, busted_one, busted_two, busted_three, bet, wallet):
    print("Hand #1")
    result_1, wallet = end_of_hand(busted_one, hand_one, dealer_hand, bet, wallet)
    print("Hand #2")
    result_2, wallet = end_of_hand(busted_two, hand_two, dealer_hand, bet, wallet)
    print("Hand #3")
    result_3, wallet = end_of_hand(busted_three, hand_three, dealer_hand, bet, wallet)
    return wallet, result_1, result_2, result_3


def scen_3_split(dealer_hand, hand_one, hand_two, hand_four, busted_one, busted_two, busted_four, bet, wallet):
    print("Hand #1")
    result_1, wallet = end_of_hand(busted_one, hand_one, dealer_hand, bet, wallet)
    print("Hand #2")
    result_2, wallet = end_of_hand(busted_two, hand_two, dealer_hand, bet, wallet)
    print("Hand #4")
    result_4, wallet = end_of_hand(busted_four, hand_four, dealer_hand, bet, wallet)
    return wallet, result_1, result_2, result_4


def scen_4_split(dealer_hand, hand_one, hand_two, hand_three, hand_four, busted_one, busted_two, busted_three,
                 busted_four, bet, wallet):
    print("Hand #1")
    result_1, wallet = end_of_hand(busted_one, hand_one, dealer_hand, bet, wallet)
    print("Hand #2")
    result_2, wallet = end_of_hand(busted_two, hand_two, dealer_hand, bet, wallet)
    print("Hand #3")
    result_3, wallet = end_of_hand(busted_three, hand_three, dealer_hand, bet, wallet)
    print("Hand #4")
    result_4, wallet = end_of_hand(busted_four, hand_four, dealer_hand, bet, wallet)
    return wallet, result_1, result_2, result_3, result_4


def end_of_hand_split(busted, player_hand, dealer_hand, shuffled_deck, bet, scenario_num, busted_one, busted_two,
                      busted_three, busted_four, hand_one, hand_two, hand_three, hand_four, wallet):
    result_1, result_2, result_3, result_4 = 0, 0, 0, 0
    if scenario_num == 1:
        wallet, result_1, result_2 = scen_1_split(dealer_hand, hand_one, hand_two, busted_one, busted_two, bet, wallet)
    if scenario_num == 2:
        wallet, result_1, result_2, result_3 = scen_2_split(dealer_hand, hand_one, hand_two, hand_three, busted_one, busted_two,
                                                    busted_three, bet, wallet)
    if scenario_num == 3:
        wallet, result_1, result_2, result_4 = scen_3_split(dealer_hand, hand_one, hand_two, hand_four, busted_one, busted_two,
                                                    busted_four, bet, wallet)
    if scenario_num == 4:
        wallet, result_1, result_2, result_3, result_4 = scen_4_split(dealer_hand, hand_one, hand_two, hand_three, hand_four,
                                                              busted_one, busted_two, busted_three, busted_four, bet,
                                                              wallet)
    result = result_1 + result_2 + result_3 + result_4
    return result, wallet


def play_game(shuffled_deck, wallet, p, wallet_track):
    game_on = True
    h_line = ""
    for i in range(50):
        h_line += '-'
    wins = 0
    total = 0
    print("You have $", wallet, "in your wallet")
    while game_on is True:
        print(h_line)
        # bet = input("How much would you like to bet this hand?")
        bet = 12
        scenario_num = 0
        dealer_hand, player_hand, shuffled_deck = act_funcs.first_deal(shuffled_deck)
        shuffled_deck, busted, split, scenario_num, busted_one, busted_two, busted_three, busted_four, hand_one, hand_two, hand_three, hand_four = start_of_hand(
            player_hand, dealer_hand, shuffled_deck, bet, p)
        dealer_hand, shuffled_deck = act_funcs.dealers_turn(dealer_hand, shuffled_deck)
        if scenario_num == 0:
            result, wallet = end_of_hand(busted, player_hand, dealer_hand, bet, wallet)
        else:
            result, wallet = end_of_hand_split(busted, player_hand, dealer_hand, shuffled_deck, bet, scenario_num, busted_one,
                                       busted_two, busted_three, busted_four, hand_one, hand_two, hand_three, hand_four,
                                       wallet)
        wins = wins + result
        total = total + 1
        wallet_track.append(wallet)
        print(total)
        print("You have $", wallet, "in your wallet")
        #choice = input("Another hand?")
        choice = 'Y'
        if total < 100:
           choice = 'Y'
        else:
           choice = 'N'
        if choice not in ('Yes', 'yes', 'y', 'Y', 'sure', 'Sure', 'yup'):
            game_on = False

    return shuffled_deck, wallet, wins, total, wallet_track
