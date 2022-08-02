from pygame import mixer
from datetime import datetime
import time

print("\033[97;1m===============Well-Come in the Health Manager Tool===============\n")
user_name = input("\033[91;1mEnter your name :  ")
set_water_interval = float(input("\033[96;1m \nSet time interval for drink the water [In hours] :  "))
set_water_quantity = float(input("\033[93;1m Set Water quantity [In ml] :  "))

set_Eye_exercise_interval = float(input("\033[96;1m \nSet time interval for your Eyes Exercises [In hours] :  "))
set_Eye_exercise_number = float(input("\033[93;1m Set number of exercises for eyes :  "))

set_physical_interval = float(input("\033[96;1m \nSet time interval for the physical activity [In hours] :  "))
set_physical_activity_number = float(input("\033[93;1m Set number of exercises for physical activity :  "))

print("\033[32;1m \nYour Health Remainder Has Been Created Successfully! \n\n")

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

def log_now(msg):
    with open("mylogs.txt", "a") as f:
        f.write(f"{user_name} :  {msg}  {datetime.now()}\n")
        print()

if __name__ == '__main__':
    init_water = time.time()
    init_eyes = time.time()
    init_exercises = time.time()

    water_seconds = set_water_interval * 5
    eyes_seconds = set_Eye_exercise_interval * 10
    exercise_seconds = set_physical_interval * 15

    while True:
        if time.time() - init_water > water_seconds:
            print(f"\033[96;1mTime for drink the water: {set_water_quantity} ml. ")
            print(f"\033[91;1mType 'drank' to stop the alarm if you have drank the {set_water_quantity} ml water \n")
            music_on_loop("water.mp3", "drank")
            init_water = time.time()
            log_now(" Drank water at :  ")

        if time.time() - init_eyes > eyes_seconds:
            print(f"\033[96;1mTime for {set_Eye_exercise_number} eyes exercises. ")
            print(f"\033[91;1mType 'done' to stop the alarm if {set_Eye_exercise_number} eyes exercises has been completed \n")
            music_on_loop("eyes.mp3", "done")
            init_eyes = time.time()
            log_now(" Done the eyes exercise at :  ")

        if time.time() - init_exercises > exercise_seconds:
            print(f"\033[96;1mTime for physical exercises. ")
            print(f"\033[91;1mType 'done' to stop the alarm if {set_physical_activity_number} physical exercises has been completed \n")
            music_on_loop("physical.mp3", "done")
            init_exercises = time.time()
            log_now(" Complete the physical exercises at :  ")
