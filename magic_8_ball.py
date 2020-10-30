from microbit import *
import random

while True:
    if accelerometer.was_gesture('shake'):
        number = random.randint(1, 6)
        if number == 1:
            display.show(Image.HAPPY)
        elif number == 2:
            display.show(Image.SAD)
        elif number == 3:
            display.show(Image.YES)
        elif number == 4:
            display.show(Image.NO)
        elif number == 5:
            display.show(Image(
                "09990:"
                "90009:"
                "00090:"
                "00000:"
                "00900:"))
        else:
            display.show(Image(
                "00000:"
                "09090:"
                "00000:"
                "99999:"
                "00000:"))