from microbit import *
import speech
import music
compass.calibrate()


while True:
    if display.read_light_level() > 0:
        speech.say("Mauw!")
        display.show(Image(
            "09090:"
            "90909:"
            "00000:"
            "00900:"
            "09990"))
    elif button_a.was_pressed():
        display.scroll(str(compass.heading()))
    elif button_b.was_pressed():
        music.play(music.ENTERTAINER)

        