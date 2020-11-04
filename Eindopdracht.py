#De verhaal stukken tekst zijn nog niet verwerkt in dit bestand!

import time


def uitleg():
    print("Hoi en welcome.\n Dit is een soort kies je eigen avontuur spel")
    print("Je krijgt steeds een stuk verhaal en daarna een keuze over wat je wilt doen")
    print("Aan de hand van keuzes die je maakt word bepaald welk einde je krijgt\n Er zijn in totaal 4 verschillende eindes en 21 verhaalstukken.")
    disclamer()


def disclamer():
    time.sleep(2)
    print("\nNog even voor dat we gaan beginnen een disclamer.")
    print("Dit is gemaakt als schoolopdracht voor de opleindig software developer op het Mediacollege Amsterdam in het begin van leerjaar 1.")
    print("Er is inspiratie genomen van verhalen van vluchtelingen van de website: \nhttps://www.vluchtelingenwerk.nl/persoonlijke-verhalen/vluchtelingen")
    print("Ondanks dat er inspiratie van is genomen van verhalen wil ik duidelijk maken dat dit verhaal niet echt gebeurd is!")
    Start()
    

def Start():
    print("\nJe woont in een rustig dorpje maar heb al vaak woorden gehad met een paar mensen die politiek een andere mening hebben. \nNa een dag werken kom je thuis aan alleen om het in vlammen op te zien gaan.")
    print("Een gerucht gaat het dorp rond dat dit het werk is geweest van de groep mensen onder andere degene waarmee je woorden heb gehad.")
    print("het schijnt dat ze af willen van iedereen met een andere mening en dit al vaker succesvol hebben gedaan.")
    print("Nog een ander probleem is dat ze aanhangers door het hele land hebben.")
    print("\nMaar nu sta jij op hun lijst en moet je er toch levend vanaf zien te komen.")
    print("\nWat ga je doen? \nA. Je blijft gewoon waar je bent. \nB. Je gaat vluchten.")
    time.sleep(2)
    answer = input("Kies A of B\n")
    if answer.upper() == "A":
        Storypart14()
    elif answer.upper() == "B":
        Storypart13()
    else:
        print("Antwoord alleen met A of B.")
        start()

def Storypart01():
    print("\nDit is verhaalstuk 1")
    time.sleep(2)
    answer = input("Kies A of B\n")
    if answer.upper() == "A":
        Storypart04()
    elif answer.upper() == "B":
        Storypart04()
    else:
        print("Antwoord alleen met A of B.")
        Storypart01()

def Storypart02():
    print("\nDit is verhaalstuk 2")
    time.sleep(2)
    answer = input("Kies A, B of C\n")
    if answer.upper() == "A":
        Storypart18()
    elif answer.upper() == "B":
        Storypart21()
    elif answer.upper() == "C":
        Storypart01()
    else:
        print("Antwoord alleen met A, B of C.")
        Storypart()

def Storypart03():
    print("\nDit is verhaalstuk 3")
    time.sleep(2)
    answer = input("Kies A of B\n")
    if answer.upper() == "A":
        Storypart11()
    elif answer.upper() == "B":
        Storypart17()
    else:
        print("Antwoord alleen met A of B.")
        Storypart03()

def Storypart04():
    print("\nDit is verhaalstuk 4")
    time.sleep(2)
    answer = input("Kies A of B\n")
    if answer.upper() == "A":
        Storypart10()
    elif answer.upper() == "B":
        Storypart08()
    else:
        print("Antwoord alleen met A of B.")
        Storypart04()

def Storypart05():
    print("\nDit is verhaalstuk 5")
    time.sleep(2)
    Ending01()

def Storypart06():
    print("\nDit is verhaalstuk 6")
    time.sleep(2)
    answer = input("Kies A of B\n")
    if answer.upper() == "A":
        Storypart04()
    elif answer.upper() == "B":
        Storypart04()
    else:
        print("Antwoord alleen met A of B.")
        Storypart06()

def Storypart07():
    print("\nDit is verhaalstuk 7")
    time.sleep(2)
    Ending02()

def Storypart08():
    print("\nDit is verhaalstuk 8")
    time.sleep(2)
    Storypart10()

def Storypart09():
    print("\nDit is verhaalstuk 9")
    time.sleep(2)
    answer = input("Kies A of B\n")
    if answer.upper() == "A":
        Storypart20()
    elif answer.upper() == "B":
        Storypart16()
    else:
        print("Antwoord alleen met A of B.")
        Storypart09()

def Storypart10():
    print("\nDit is verhaalstuk 10")
    time.sleep(2)
    answer = input("Kies A of B\n")
    if answer.upper() == "A":
        Storypart09()
    elif answer.upper() == "B":
        Storypart15()
    else:
        print("Antwoord alleen met A of B.")
        Storypart10()

def Storypart11():
    print("\nDit is verhaalstuk 11")
    time.sleep(2)
    Ending01()

def Storypart12():
    print("\nDit is verhaalstuk 12")
    time.sleep(2)
    answer = input("Kies A of B\n")
    if answer.upper() == "A":
        Storypart06()
    elif answer.upper() == "B":
        Storypart03()
    else:
        print("Antwoord alleen met A of B.")
        Storypart12()

def Storypart13():
    print("\nDit is verhaalstuk 13")
    time.sleep(2)
    answer = input("Kies A of B\n")
    if answer.upper() == "A":
        Storypart05()
    elif answer.upper() == "B":
        Storypart19()
    else:
        print("Antwoord alleen met A of B.")
        Storypart13()

def Storypart14():
    print("\nJe hebt even geprobeert om te doen of er niks aan de hand is, maar je trekt het niet meer. \nJe besluit om alles achter te laten en het land uit te vluchten.")
    print("/n")
    time.sleep(2)
    answer = input("Kies A of B\n")
    if answer.upper() == "A":
        Storypart02()
    elif answer.upper() == "B":
        Storypart13()
    else:
        print("Antwoord alleen met A of B.")
        Storypart14()

def Storypart15():
    print("\nDit is verhaalstuk 15")
    time.sleep(2)
    Ending01()

def Storypart16():
    print("\nDit is verhaalstuk 16")
    time.sleep(2)
    Ending03()

def Storypart17():
    print("\nDit is verhaalstuk 17")
    time.sleep(2)
    Ending01()

def Storypart18():
    print("\nDit is verhaalstuk 18")
    time.sleep(2)
    answer = input("Kies A of B\n")
    if answer.upper() == "A":
        Storypart10()
    elif answer.upper() == "B":
        Storypart08()
    else:
        print("Antwoord alleen met A of B.")
        Storypart18()

def Storypart19():
    print("\nDit is verhaalstuk 19")
    time.sleep(2)
    answer = input("Kies A of B\n")
    if answer.upper() == "A":
        Storypart12()
    elif answer.upper() == "B":
        Storypart07()
    else:
        print("Antwoord alleen met A of B.")
        Storypart19()

def Storypart20():
    print("\nDit is verhaalstuk 20")
    time.sleep(2)
    Ending04()

def Storypart21():
    print("\nDit is verhaalstuk 21")
    time.sleep(2)
    Ending01()


def Ending01():
    print("\nHet is je gelukt om in Nederland te komen, en na veel moeite om de taal en cultuur te leren.")
    print("Ben je eindelijk veilig en ingeburgerd en mag je hier blijven.")
    time.sleep(2)
    End()

def Ending02():
    print("\nHet is je gelukt om in Nederland te komen, en je doet veel moeite om de taal en cultuur te leren.")
    print("Je bent in 6 jaar als 8 keer van plek verhuisd en wordt er een beetje gek van.")
    print("Je bent al jaren bezig om een verblijfs vergunning te krijgen, \nmaar je hebt het gevoel dat je steeds alleen maar van het kastje naar de muur word gestuurd.")
    time.sleep(2)
    End()

def Ending03():
    print("\nNa een paar jaar in Nederland te hebben gewoond merk je dat je thuis gewoon te veel mist.")
    print("Je hebt de laatste tijd niks meer gehoord over de mensen waarvan je bent gevlucht, \nen maakt de beslissing om terug te gaan.")
    print("Eenmaal terug lijkt alles in eerste instantie normaal.")
    print("Maar binnen 3 maanden staan ze weer voor je neus en begint alles van voor af aan.")
    time.sleep(2)
    End()

def Ending04():
    print("\nDit is een goed einde")
    time.sleep(2)
    End()


def End():
    print("\nDit is het einde. \nWil je het opnieuw proberen? \nA = Ja \nB = Nee")
    time.sleep(2)
    answer = input("Kies A of B\n")
    if answer.upper() == "A":
        Start()
    elif answer.upper() == "B":
        Credits()
    else:
        print("Antwoord alleen met A of B.")
        End()


def Credits():
    print("\nDit is het einde dan, Hier scheiden onze weggen...")
    print("Ik hoop dat je het leuk vond.")
    time.sleep(2)
    print("\nGemaakt door: Monique Wienholds")
    print("In opdracht van: Rosmerta Goei & Ed Schenk")
    print("Mede mogelijk gemaakt door: Mediacollege Amsterdam")
    print("Met speciale dank aan: Stichting VluchtelingenWerk Nederland")
    print("\nEn natuurlijk heel veel dank aan jou voor het spellen!")

uitleg()

