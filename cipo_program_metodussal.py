from Cipo import Cipo
def peldanyok_listaban():
    peldany1 = Cipo("Nike",42)
    peldany2 = Cipo("Adidas",41)
    peldany3 =  Cipo("Adidas",45)

    cipok = []
    cipok.append(peldany1)
    cipok.append(peldany2)
    cipok.append(peldany3)
    return cipok





def lista_kiir(lista):
    for i in range(0,len(lista),1):
        nev = lista[i].nev
        meret = lista[i].meret
        print(f"{nev}  ({meret})")

#Ez a rövid verzió:
"""        
lista_kiir(peldanyok_listaban())
"""
cipok_lista = peldanyok_listaban()
lista_kiir(cipok_lista)


def osszegzes_tetele(cipok):                               #összegzés tétele
    ossz:int = 0
    for i in range(0,len(cipok),1):
        ossz += cipok[i].meret
    print(round(ossz/len(cipok), 3))

osszegzes_tetele(cipok_lista)




def eldontes_tetel(cipok):                                #eldöntés tétele
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
def maximum_kivakasztas_tetel(cipok):
    print("Milyen márkájú a legnagyobb cipő: ", end="")
    legnagyobb_helye:int = 0
    
    for i in range(0,len(cipok),1):
        if cipok[i].meret > cipok[legnagyobb_helye].meret:
            legnagyobb_helye = i
    print(cipok[legnagyobb_helye].nev)



    #hány db adidas cipő van                                                #megszámlálás tétele
def megszamlalas_tetel(cipo):          
    szamlalo:int = 0 
    print(f"\tHány olyan cipő van ami adidas:")
    for i in range(0,len(cipok),1):
        if cipok[i].nev == "Adidas":
            szamlalo += 1
    print(f"{szamlalo} db")
    
