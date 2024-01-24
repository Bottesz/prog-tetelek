from Cipo import Cipo
import math

peldany1 = Cipo("Nike",42)
peldany2 = Cipo("Adidas",41)
peldany3 =  Cipo("Adidas",45)

cipok = []
cipok.append(peldany1)
cipok.append(peldany2)
cipok.append(peldany3)
for i in range(0,len(cipok),1):
    nev = cipok[i].nev
    meret = cipok[i].meret
    print(f"{nev}  ({meret})")

def cipo_atlag():                               #összegzés tétele
    ossz:int = 0
    for i in range(0,len(cipok),1):
        ossz += cipok[i].meret
    print(round(ossz/len(cipok), 3))

cipo_atlag()

def nagyobb42adidas():
    db: int = 0
    for i in range(0,len(cipok), 1):
        if cipok[i].meret < 42:
            db += 1
    print(db)

nagyobb42adidas()




def nagyobb42():                                #eldöntés tétele
    print("Van-e 42-nél nagyobb Adidas: ")
    van = False
    for i in range(0,len(cipok),1):
        if cipok[i].nev == "Adidas" and cipok[i].meret < 42:
            van = True
    if van ==False:
        print("Van")
    else:
        print("Nincs")



# Melyik a legnagyobb cipő                      #maximum kiválasztás tétele
def legnagyobb_marka_cipo():
    print("Milyen márkájú a legnagyobb cipő: ", end="")
    legnagyobb_helye:int = 0
    
    for i in range(0,len(cipok),1):
        if cipok[i].meret > cipok[legnagyobb_helye].meret:
            legnagyobb_helye = i
    print(cipok[legnagyobb_helye].nev)



    #hány db adidas cipő van                                                #megszámlálás tétele
def hany_db_adidas():          
    szamlalo:int = 0 
    print(f"\tHány olyan cipő van ami adidas:")
    for i in range(0,len(cipok),1):
        if cipok[i].nev == "Adidas":
            szamlalo += 1
    print(f"{szamlalo} db")
    
    
    


    