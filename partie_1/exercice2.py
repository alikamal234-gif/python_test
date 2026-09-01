employee = input("nom de employe : ") 
salaire = int(input("son salaire par heur (DH) : ") )
heures_travaille = int(input("nombre d'heure de travaille: ") )


if heures_travaille <= 40:
    print(f" le salaire est : {salaire * heures_travaille} DH")
else :
    heures_sur_quaront = (heures_travaille - 40 ) * 1.5
    print(f"le salaire est : { 40 * salaire + heures_sur_quaront} DH")
