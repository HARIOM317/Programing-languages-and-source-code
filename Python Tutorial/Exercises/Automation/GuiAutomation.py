from cv2 import imread
from gui_automation import GuiAuto
import pyautogui

Gcurser = GuiAuto()

def start():
    if Gcurser.detect(imread('.\Icons\Recycle_Bin.png'), 0.6):
        Gcurser.click()
        # pyautogui.doubleClick()   # For double click
        pyautogui.rightClick()      # For right click

        if Gcurser.detect(imread('.\Icons\Empty.png'), 0.6):
            Gcurser.click()
            if Gcurser.detect(imread('.\Icons\Yes.png'), 0.4):
                Gcurser.click()

start()
