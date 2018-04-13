from actions import act_funcs


def start_of_hand(player_hand, dealer_hand, shuffled_deck):
    if act_funcs.dealer_win_check(dealer_hand) is True:
        print("Dealer has Blackjack! Everybody loses.")
        print("Their cards were:", dealer_hand[0], "and", dealer_hand[1])
    else:
        print("Dealer holds a hidden card and a", dealer_hand[1])
        print("Your cards are:")
        print(player_hand[0], " : ", player_hand[1])
        print("You have", act_funcs.score_hand(player_hand), "points")
        shuffled_deck, busted, player_hand = act_funcs.run_player_turn(player_hand, shuffled_deck)
        return shuffled_deck, busted


def end_of_hand(busted, player_hand, dealer_hand, shuffled_deck):
    if busted is False:
        dealer_hand, shuffled_deck = act_funcs.dealers_turn(dealer_hand, shuffled_deck)
        if act_funcs.score_hand(dealer_hand) > 21:
            print("Dealer busts! Everybody wins")
        elif act_funcs.score_hand(player_hand) > act_funcs.score_hand(dealer_hand):
            print("Player wins!")
        elif act_funcs.score_hand(dealer_hand) == act_funcs.score_hand(player_hand):
            print("Push")
        else:
            print("Player loses.")
        print("Final score:")
        hand_print = ''
        for i in range(0,len(dealer_hand)):
            hand_print += str(dealer_hand[i].value) + ' of ' + dealer_hand[i].suit + ', '
        print("Dealer Hand:", hand_print[:-2], '- Final Score: ', act_funcs.score_hand(dealer_hand))
        hand_print = ''
        for i in range(0, len(player_hand)):
            hand_print += str(player_hand[i].value) + ' of ' + player_hand[i].suit + ', '
        print("Player Hand:", hand_print[:-2], '- Final Score: ', act_funcs.score_hand(player_hand))


def play_game(shuffled_deck):
    game_on = True
    h_line = ""
    for i in range(100):
        h_line += '-'
    while game_on is True:
        print(h_line)
        dealer_hand, player_hand, shuffled_deck = act_funcs.first_deal(shuffled_deck)
        dealer_points = act_funcs.score_hand(dealer_hand)
        shuffled_deck, busted = start_of_hand(player_hand, dealer_hand, shuffled_deck)
        end_of_hand(busted, player_hand, dealer_hand, shuffled_deck)
        choice = input("Another hand?")
        if choice not in ('Yes', 'yes', 'y', 'Y', 'sure', 'Sure', 'yup'):
            game_on = False

    return dealer_hand, player_hand, shuffled_deck
