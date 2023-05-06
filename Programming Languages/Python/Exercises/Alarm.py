import datefinder
from pygame import mixer
import datetime

def music_on_loop(file, stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    user_input = input()
    while True:
        if user_input == stopper:
            mixer.music.stop()
            break
        else:
            print("\033[91;1m Oho.. You entered wrong input but no problem!")
            mixer.music.stop()
            break

def alarm(text):
    dateTimeAlarm = datefinder.find_dates(text)
    for match in dateTimeAlarm:
        print(match)
    stringA = str(match)
    timeA = stringA[11:]
    hour = timeA[:-6]
    hour = int(hour)
    minutes = timeA[3:-3]
    minutes = int(minutes)

    while True:
        if hour == datetime.datetime.now().hour:
            if minutes == datetime.datetime.now().minute:
                print("Type 'done' for stop the alarm :   ")
                music_on_loop("Physical.mp3", "done")
            elif minutes < datetime.datetime.now().minute:
                break


alarm("set alarm at 3:48 pm")
alarm("set alarm at 3:51 pm")
