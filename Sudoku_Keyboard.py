from pynput.keyboard import key, Controller
from time import sleep


keyboard = Controller()

def keyboard_usage(value):

    keyboard.press(value)
    sleep(1)
    keyboard.release(value)
    sleep(1)