notes_etudiants = {"Omar": 15, "Sara": 8, "Yassine": 17, "Imane": 11, "Hamza": 6, "Nadia": 14}

notes_infer = {}
notes_super = {}

for key , value in notes_etudiants.items():
    if value < 10 :
        notes_infer[key] = value
    else : 
        notes_super[key] = value
nom_key = ""
max = 0
print(notes_infer , notes_super)
for key , value in notes_super.items():
    if max < value :
        max = value
        nom_key = key
print(f"porcentage de reussite : {max / len(notes_etudiants)} \nle meilleur etudiant : {nom_key}")