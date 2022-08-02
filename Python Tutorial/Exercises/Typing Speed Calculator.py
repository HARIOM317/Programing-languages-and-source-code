from time import *
import random as r

def mistakes(paragraph, user_entry):
    error = 0
    for i in range(len(paragraph)):
        try:
            if paragraph[i] != user_entry[i]:
                error += 1
        except:
            error += 1
    return error

def typing_speed(starting_time, ending_time, user_input):
    time_diff = ending_time - starting_time
    time_round = round(time_diff, 2)
    speed = len(user_input) / time_round
    return round(speed)

if __name__ == '__main__':
    while True:
        Ready = input("\033[98;1m \nReady For Test (Y/N) :  ")
        if Ready == 'Y' or Ready == 'y':
            test = ["Python is a general-purpose, popular programming language and it is used in almost every technical field.",
                    "Python is easy to learn yet powerful and versatile scripting language, which makes it attractive for Application Development.",
                    "Python makes the development and debugging fast because there is no compilation step included in Python.",
                    "development, and edit-test-debug cycle is very fast.",
                    "Python is easy to learn yet powerful and versatile scripting language, which makes it attractive."
                    ]
            test1 = r.choice(test)
            print(f"\033[96;1m                                               _____***** Typing Speed *****_____ ",
            "\033[91;1m \nParagraph: ", f"\033[93;1m {test1} \n ")

            time_1 = time()
            userInput = input("\033[92;1mEnter Paragraph :  ")
            time_2 = time()

            print("\033[93;1m \nYOUR RESULT: \n")
            print("\033[95;1m          Speed :  ", typing_speed(time_1, time_2, userInput), "WPS")
            print("\033[95;1m          Mistakes :  ", mistakes(test1, userInput))

        elif Ready == 'N' or Ready == 'n':
            print('\033[93;1m THANK YOU!')
            exit()

        else:
            print("\033[98;1m \nInvalid Input!")
