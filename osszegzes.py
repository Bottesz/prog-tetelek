def osszegzes_tetel():
    n:int = 0
    i:int = 0
    ossz = 0
    
    while (n <= 0): 
        n:int = int(input("N: "))
    for i in range(0, n+1):
            ossz += 1 
    print(f"Az első {n} db természetes szám összege: {ossz}")


def szorzas_tetel():
    n:int = 0
    i:int = 0
    ossz = 0
    
    while (n <= 0): 
        n:int = int(input("N: "))
    for i in range(0, n+1):
            ossz *= 1 
    print(f"Az első {n} db természetes szám összege: {ossz}")




     



