import time

print("Hello you! Ik ben Monique.")
print("wie ben jij?")

jouNaam = input("Jou naam is:\n")

print("Hey " + jouNaam, "leuk je te zien!")
time.sleep(1)
print("We gaan een spelletje spelen.")

print("Heb je er zin in?")
antwoord01 = input ("schrijf Ja of Nee: \n")
if antwoord01 == "Ja" or antwoord01 == "ja":
     print("Gezellig, laten we beginnen!")
if antwoord01 == "Nee" or antwoord01 == "nee":
     print("Jammer joh we gaan het toch doen.")

time.sleep(1)
print("vraag 1. Hoe oud ben ik nu?")
time.sleep(1)
antwoord02 = input ("kies uit: \nA.16 \nB.18 \nC.19 \nD.20 \n")

if antwoord02 == "A" or antwoord02 == "a":
     print("Dit klopt niet, sorry man.")
if antwoord02 == "B" or antwoord02 == "b":
     print("Bijna goed, maar niet helemaal")
if antwoord02 == "C" or antwoord02 == "c":
     print("Yay! Dit klopt gefeliciteerd.")
if antwoord02 == "D" or antwoord02 == "d":
     print("Als je volgend jaar hetzelfde zou antwoorden heb je het goed.")

time.sleep(1)
print("vraag 2. Hoe heet mijn konijn die ik nu heb?")
time.sleep(1)
antwoord03 = input ("kies uit: \nA.Pluisje \nB.Brownie \nC.Stampertje \n")

if antwoord03 == "A" or antwoord03 == "a":
     print("Net niet goed, Pluisje was mijn eerste konijn.")
if antwoord03 == "B" or antwoord03 == "b":
     print("Brownie is idderdaad de naam van mijn konijn!")
if antwoord03 == "C" or antwoord03 == "c":
     print("Leuk geprobeert, maar ik heb nog nooit een konijn gehad met deze naam.")

time.sleep(1)
print("vraag 3. Wat is zijn mijn favorite kleuren?")
time.sleep(1)
antwoord04 = input ("kies uit: \nA.Neon \nB.Pastel \nC.zwart/wit \n")

if antwoord04 == "A" or antwoord04 == "a":
     print("Goed gedaan. Ik ben dol elke kleur die schreeuwt.")
if antwoord04 == "B" or antwoord04 == "b":
     print("Pastel kleuren zijn mooi, maar ik heb er niet veel mee.")
if antwoord04 == "C" or antwoord04 == "c":
     print("Ik heb niks met zwart/wit.")
time.sleep(1)
print("Bedankt voor het spelen. Tot de volgende keer.")