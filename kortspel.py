print(" ♣ Välkommen till finns i sjön ♣ \n")
print("1.Starta\n"
+"2.Avsluta\n")

# ♠ ♥ ♦ ♣

hjärter = 0
spader = 0
klöver = 0
ruter = 0

meny = 0
meny2 = 0

while meny != 2:
    
    try:
        meny = int(input("Gör ett val: "))
    except:
        print("\nDu måste ange en siffra!\n")
    
    if meny == 1:
        print("\nLOADING...\n"
        +"\nLOADING..\n"
        +"\nLOADING...\n")
        print("\nDå kör vi\n")
        if meny2 == 1:
            print("verynice")

    elif meny == 2:
        print ("\nSes snart igen\n")






