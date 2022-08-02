import random

print("\033[91;1m***** Well-Come to the Snack-Water-Gun Game *****")
print("\033[92;1mNote:- There will be 10 rounds between you and computer!\n")
Name = input("\033[35;1mEnter your name: ")
option = ['S', 'W', 'G']
while True:
    i = 1
    user_score = 0
    computer_score = 0
    while i <= 10:
        computer_choice = random.choice(option)
        print("\n")
        user_choice = input(
            "\033[92;1mEnter 'S' for Snack, 'W' for Water, and 'G' for Gun: ")

        if computer_choice == 'S' and user_choice == 'S':
            print(f"\033[94;1mDraw! this round. " "You choose ", {user_choice}, "and computer choose ",
                  {computer_choice})
            print("\033[93;1m*** Dono Sap aapas me mar mite ***")
            print("\033[95;1m", Name, "Score is: ", user_score)
            print("\033[95;1mComputer Score is: ", computer_score)

        elif computer_choice == 'S' and user_choice == 'W':
            print(f"\033[94;1mYou Lose! this round. " "You choose ", {user_choice}, "and computer choose ",
                  {computer_choice})
            print("\033[93;1m*** Sap pura pani pi gaya ***")
            computer_score += 1
            print("\033[95;1m", Name, "Score is: ", user_score)
            print("\033[95;1mComputer Score is: ", computer_score)

        elif computer_choice == 'S' and user_choice == 'G':
            print(f"\033[94;1mYou Won! this round. " "You choose ", {user_choice}, "and computer choose ",
                  {computer_choice})
            print("\033[93;1m*** Gun ne sap ko fod diya ***")
            user_score += 1
            print("\033[95;1m", Name, "Score is: ", user_score)
            print("\033[95;1mComputer Score is: ", computer_score)

        elif computer_choice == 'W' and user_choice == 'S':
            print(f"\033[94;1mYou Won! this round. " "You choose ", {user_choice}, "and computer choose ",
                  {computer_choice})
            print("\033[93;1m*** Sap pura pani pi gaya ***")
            user_score += 1
            print("\033[95;1m", Name, "Score is: ", user_score)
            print("\033[95;1mComputer Score is: ", computer_score)

        elif computer_choice == 'W' and user_choice == 'W':
            print(f"\033[94;1mDraw! this round. " "You choose ", {user_choice}, "and computer choose ",
                  {computer_choice})
            print(
                "\033[93;1m*** Pani-Pani mil gaye aur dono me dosti ho gayi ***")
            print("\033[95;1m", Name, " Score is: ", user_score)
            print("\033[95;1mComputer Score is: ", computer_score)

        elif computer_choice == 'W' and user_choice == 'G':
            print(f"\033[94;1mYou Lose! this round. " "You choose ", {user_choice}, "and computer choose ",
                  {computer_choice})
            print("\033[93;1m*** Gun pani me dub gayi ***")
            computer_score += 1
            print("\033[95;1m", Name, " Score is: ", user_score)
            print("\033[95;1mComputer Score is: ", computer_score)

        elif computer_choice == 'G' and user_choice == 'S':
            print(f"\033[94;1mYou Lose! this round. " "You choose ", {user_choice}, "and computer choose ",
                  {computer_choice})
            print("\033[93;1m*** Gun ne sap ko fod diya ***")
            computer_score += 1
            print("\033[95;1m", Name, " Score is: ", user_score)
            print("\033[95;1mComputer Score is: ", computer_score)

        elif computer_choice == 'G' and user_choice == 'W':
            print(f"\033[94;1mYou Won! this round. " "You choose ", {user_choice}, "and computer choose ",
                  {computer_choice})
            print("\033[93;1m*** Gun pani me dub gayi ***")
            user_score += 1
            print("\033[95;1m", Name, " Score is: ", user_score)
            print("\033[95;1mComputer Score is: ", computer_score)

        elif computer_choice == 'G' and user_choice == 'G':
            print(f"\033[94;1mDraw! this round. " "You choose ", {user_choice}, "and computer choose ",
                  {computer_choice})
            print("\033[93;1m*** Banduk ne banduk ko hi fod dala ***")
            print("\033[95;1m", Name, " Score is: ", user_score)
            print("\033[95;1mComputer Score is: ", computer_score)

        else:
            print("\033[91;1mInvalid input")

        i += 1

    if user_score > computer_score:
        print(f"\033[96;1m\nCongratulation You won this game" "\nyour score is: ", {user_score},
              "\nComputer score is: ", {computer_score})

    elif user_score < computer_score:
        print(f"\033[96;1m\nOpps! You lose this game" "\nyour score is: ", {user_score}, "\nComputer score is: ",
              {computer_score})

    else:
        print(f"\033[96;1m\nMatch draw!" "\nyour score is: ", {
              user_score}, "\nComputer score is: ", {computer_score})

    replay = input("\033[94;1mDo you want to play again? (Y/N): ")

    if replay == 'y' or replay == 'Y':
        continue
    elif replay == 'n' or replay == 'N':
        break
    else:
        print("\033[91;1mInvalid input")
