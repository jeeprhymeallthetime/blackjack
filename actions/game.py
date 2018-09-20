from actions import act_funcs


def start_of_hand(player_hand, dealer_hand, shuffled_deck, bet, p):
    busted = False
    if act_funcs.dealer_win_check(dealer_hand) is True:
        print("Dealer has Blackjack! Everybody loses.")
        print("Their cards were:", dealer_hand[0], "and", dealer_hand[1])
    else:
        print("Dealer holds a hidden card and a", dealer_hand[1])
        print("Your cards are:")
        print(player_hand[0], " : ", player_hand[1])
        print("You have", act_funcs.score_hand(player_hand), "points")
        shuffled_deck, busted, player_hand = act_funcs.run_player_turn_auto(player_hand, dealer_hand, shuffled_deck, p)
    return shuffled_deck, busted


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
        dealer_hand, player_hand, shuffled_deck = act_funcs.first_deal(shuffled_deck)
        shuffled_deck, busted = start_of_hand(player_hand, dealer_hand, shuffled_deck, bet, p)

        result = end_of_hand(busted, player_hand, dealer_hand, shuffled_deck, bet)
        wins = wins + result
        total = total + 1
        print(total)
        #choice = input("Another hand?")
        choice = 'Y'
        if total < 100:
            choice = 'Y'
        else:
            choice = 'N'
        if choice not in ('Yes', 'yes', 'y', 'Y', 'sure', 'Sure', 'yup'):
            game_on = False

    return shuffled_deck, wallet, wins, total
