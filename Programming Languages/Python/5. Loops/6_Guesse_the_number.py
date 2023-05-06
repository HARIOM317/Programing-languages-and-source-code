num = 71
no_Of_Guesses = 0
while 1:
    guesses = int(input("Enter a number between 1-100 : "))
    no_Of_Guesses += 1
    if no_Of_Guesses >= 10:
        print("\nGuesses = ", no_Of_Guesses)
        print("Oho! You have been used all lifelines!")
        break
    else:
        if guesses > num:
            print("\nGuesses = ", no_Of_Guesses)
            print("Lower number please! ")
            continue

        elif guesses < num:
            print("\nGuesses = ", no_Of_Guesses)
            print("Higher number please! ")
            continue
        else:
            print("\nCongratulation! You guessed correct number in ", no_Of_Guesses, " trials")
            break
