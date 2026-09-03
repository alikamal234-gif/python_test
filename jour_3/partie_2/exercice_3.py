

def calculer_carre(nomber) :
    """"this fnction return number carre from the parametre and dosn't accept number negatif and another value like string and bool"""
    try :
        assert int(nomber) > 0
        print("resultat est : " , int(nomber) ** 2)
    except ValueError as v:
        print("Le paramètre doit être un nombre")
    except AssertionError as a :
        print("Le nombre ne peut pas être négatif")
    finally :
        print("programme est fini")


calculer_carre(4)
calculer_carre("quatre")
calculer_carre(-2)