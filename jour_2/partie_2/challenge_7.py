etudiants = [
 {"nom": "Omar", "age": 22, "note": 15},
 {"nom": "Sara", "age": 21, "note": 17},
 {"nom": "Yassine", "age": 23, "note": 9},
 {"nom": "Imane", "age": 20, "note": 13},
 {"nom": "Hamza", "age": 24, "note": 7}
]


admis = []
echec = []
sum_note = 0
meilleur_note =0
for i in etudiants : 
    sum_note += i["note"]
    if meilleur_note < i["note"] :
        meilleur_note = i["note"]
    if i["note"] < 10 : 
        echec.append(i)
    else : 
        admis.append(i)
moyen_classe = sum_note /len(etudiants)
print(f"etudiant admis c'est : {admis} , \net les etudiants sont echec sont : {echec} , \net le moyen de classe est {moyen_classe} , \net le meilleur note c'est {meilleur_note}")