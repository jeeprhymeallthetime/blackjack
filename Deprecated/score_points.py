#Score Hand

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