from actions import act_funcs

def play_game(dealer_hand, player_hand, shuffled_deck):
    if act_funcs.dealer_win_check(dealer_hand) is True:
        print("Dealer has Blackjack! Everybody loses.")
        print("Their cards were:", dealer_hand[0], "and", dealer_hand[1])
    else:
        print("Dealer holds a hidden card and a", dealer_hand[1])
        print("Your cards are:")
        print(player_hand[0], " : ", player_hand[1])
        print("You have", act_funcs.score_hand(player_hand), "points")
        player_points, shuffled_deck, busted = act_funcs.run_player_turn(player_hand, shuffled_deck)
        if busted is False:
            dealer_hand, shuffled_deck = act_funcs.dealers_turn(dealer_hand, shuffled_deck)
            if act_funcs.score_hand(dealer_hand) > 21:
                print("Dealer busts! Everybody wins")
            elif act_funcs.score_hand(dealer_hand) > act_funcs.score_hand(player_hand):
                print("Player wins!")
            else:
                print("Player loses.")
            print("Final score:")
            print("Dealer Hand:", dealer_hand[0], "and", dealer_hand[1])
            print("Player Hand:", player_hand[0], "and", player_hand[1])

    return dealer_hand, player_hand, shuffled_deck