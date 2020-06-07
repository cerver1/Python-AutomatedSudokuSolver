from pynput.keyboard import Key, Controller
from time import sleep

keyboard = Controller()


def keyboard_usage(value):
    keyboard.press(value)
    sleep(0.5)
    keyboard.release(value)
    sleep(0.5)
