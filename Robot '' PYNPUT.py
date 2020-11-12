from pynput.keyboard import Key, Controller

keyboard = Controller()


import sys
import os
import time

from EDITME import wrd


for x in range(len(wrd)):
    for y in wrd[x]:
        keyboard.press(y)
        keyboard.release(y)
        time.sleep(0.02)

    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
