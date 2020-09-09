import datetime

print ("Hello you!. Ik ben Monique.")
print ("wie ben jij?")

username = input("Mijn naam is:")

print ("Hey " + username, "leuk je te zien!")

x = datetime.datetime.now()

while True: 
     query = input("Wil je de datum en tijd weten? Y/N") 
     Fl = query[0].lower() 
     if query == "" or not Fl in ["y","n"]: 
        print("Antwoord asjeblieft met Y of N!") 
     else: 
        break 
if Fl == "y": 
    print("De datum en tijd is:")  
    print(x)
if Fl == "n": 
    print("Jammer, tot de volgende keer!")




