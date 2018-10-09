print(" ♣ Välkommen till finns i sjön ♣ \n")
print("1.Starta\n"
+"2.Avsluta\n")

import random

# ♠ ♥ ♦ ♣ Spader, hjärter, ruter och klöver

kort = ["Ess", "2", "3", "4", "5","6", "7", "8", "9","10", "Knekt", "Dam","Kung"]
typ = ["♠ Spader ♠"," ♥ Hjärter ♥", "♦ Ruter ♦", "♣ Klöver ♣"]

hand = []

meny = 0
meny2 = 0
 

while meny != 2:

    try:
        meny = int(input("Gör ett val: "))
    except:
        print("\nDu måste ange en siffra!\n")

    if meny == 1:
        print("\nLoading…\n"
        +"\n██ 32% \n"
        +"\n███ 49% \n"
        +"\n████ 76% \n"
        +"\n█████ 89% \n"
        +"\n██████ 100%\n"
        +"\nComplete\n")
    
    elif meny == 2:
        print ("\nSes snart igen\n")


#kort = random.randint(0, 12)

#while kort != 100:
    #typ = int(input("Vilken typ av kort: "))
    #kort = int(input("Skriv in kort: "))

#print("Välj spelare: "
#+""
#+"Visa poäng"
#+"")