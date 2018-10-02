print(" ♣ Välkommen till finns i sjön ♣ \n")
print("1.Starta\n"
+"2.Avsluta\n")

# ♠ ♥ ♦ ♣

hjärter = 0
spader = 0
klöver = 0
ruter = 0
kort = 0

meny = 0
meny2 = 0

while meny != 2:
    
    try:
        meny = int(input("Gör ett val: "))
    except:
        print("\nDu måste ange en siffra!\n") 
    if meny == 1:
       print("\nLoading…\n"
        +"\n██ 39% \n"
        +"\n███ 49% \n"
        +"\n████ 76% \n"
        +"\n█████ 89% \n"
        +"\n██████ 100%\n"
        +"\ncomplete\n")
        

        # tal = random.randint(1, 12)
         
    elif meny == 2:
        print ("\nSes snart igen\n")
    