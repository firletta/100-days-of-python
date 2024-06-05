import keyboard
from turtle import Turtle, Screen
import time
import sys

def main():
    global tim
    tim = Turtle()
    screen = Screen()

    key_mapping = {
        'w': tim.forward,
        'a': tim.left,
        's': tim.backward,
        'd': tim.right,
        'c': clear
    }

    while True:
        if keyboard.is_pressed('q'):
            sys.exit()
        for key, action in key_mapping.items():
            if keyboard.is_pressed(key):
                if key == 'c':
                    action()
                else:
                    action(10)
        time.sleep(0.1)

def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

if __name__ == "__main__":
    main()