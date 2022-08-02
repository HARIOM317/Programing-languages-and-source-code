import pyautogui
from PIL import Image, ImageGrab
# from numpy import asarray
import time

def takeScreenShot():
    image = ImageGrab.grab().convert('L')   # Convert screenshot into a black & white image
    return image

def hitKey(key):
    pyautogui.keyDown(key)
    return

def isCollide(data):
    # Draw the rectangle for birds
    for i in range(350, 400):
        for j in range(470, 640):
            if data[i, j] > 100:
                hitKey('down')
                return

    # Draw the rectangle for cactus
    for i in range(350, 400):
        for j in range(640, 700):
            if data[i, j] > 100:
                hitKey ('up')
                return
    return

if __name__ == '__main__':
    print("hey.. Dino game about to start in 3 seconds")
    time.sleep(3)
    # hitKey('up')
    while True:
        image = ImageGrab.grab().convert('L')
        data = image.load()
        isCollide(data)
'''
        # print(asarray(image))

        # Draw the rectangle for cactus
        for i in range(280, 330):
            for j in range(640, 700):
                data[i, j] = 0
    
        # Draw the rectangle for birds
        for i in range(280, 330):
            for j in range(470, 640):
                data[i, j] = 150
        image.show()
        break
'''