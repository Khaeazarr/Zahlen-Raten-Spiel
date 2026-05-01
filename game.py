import random

print("Ich denke an eine Zahl zwischen 1 und 20.")
ziel = random.randint(1, 20)
versuche = 0

while True:
    tipp = int(input("Dein Tipp: "))
    versuche += 1
    
    if tipp < ziel:
        print("Zu niedrig!")
    elif tipp > ziel:
        print("Zu hoch!")
    else:
        print(f"Gewonnen! Du hast {versuche} Versuche gebraucht.")
        break
