import pyautogui
import time
time.sleep(5)

count = 0

while count <= 10000:
    pyautogui.typewrite("Dekh I am laughing. Ha Ha Ha Ha Ha........, Count = " + str(count))
    time.sleep(0.5)
    pyautogui.press('enter')
    count = count+1
