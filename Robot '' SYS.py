import sys
import os
import time

from EDITME import wrd


for char in wrd:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(0.02)
