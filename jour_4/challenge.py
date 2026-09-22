import math 


def factorielle(n : int) -> int:
    result = int(n)
    for i in range(1,n):
        result *= i
    return result

# print(factorielle(4))

def multiplication(m : int) -> str :
    for i in range(1,11):
        print(f"{m} * {i} = {m*i}")

# multiplication(3)

def carre_parfait(L : int) -> str :
    racine = str(math.sqrt(L))
    racine = racine.split('.')
    if int(racine[1]) != 0:
        return "n'est pas un carré pafait"
    else : 
        return "un carré parfait"
        

# print(carre_parfait(5))

def chaine(*args) -> str:
    for i in args:
        print(i)

# chaine("a", "K" , "l")


def phrase(phrase : str):
    mots = phrase.split()
    long_mot = mots[0]
    for i in mots :
        if len(i) > len(long_mot):
            long_mot = i

    return long_mot

# print(phrase("ali kamal"))

def nombre_occurrences(ch):
    chaines = {}
    for i in ch :
        if i in chaines:
            chaines[i] += 1
        else :
            chaines[i] = 1
    return chaines

# for key , value in nombre_occurrences("welcome to ai leek").items():
#     print(f"\n Le caractère {key} figure {value} fois dans la chaîne Ch.")

