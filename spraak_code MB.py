# Add your Python code here. E.g.
from microbit import *
import speech
import random

lengteWoordArray = 3

onderwerp = ["Jurre", "Mike", "She"]
werkwoord = ["helps", "learns", "shops"]
rest = ["with coding", "at school", "online"]

def sayTheWords01(word):
    print(word)
    speech.say(word, speed=120, pitch=100, throat=100, mouth=200)
    sleep(500)
    
def sayTheWords02():
    willekeurigGetal = random.randint(0, lengteWoordArray - 1)
    display.show(willekeurigGetal)
    sayTheWords01(onderwerp[willekeurigGetal])
    sayTheWords01(werkwoord[willekeurigGetal])
    sayTheWords01(rest[willekeurigGetal])
    
while True:
    if button_a.is_pressed():
        display.show(Image.HAPPY)
        sayTheWords01("hallo I am happy")
    elif button_b.is_pressed():
        display.show(Image.SAD)
        sayTheWords01("why are you sad")
    elif display.read_light_level() < 40:
        sayTheWords02()
    else:
        display.show(Image.SQUARE)
        
    