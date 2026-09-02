etudiant = {
    "nom": "Omar",
    "age": 22,
    "formation": 
        {
            "nom": "Développement IA", 
            "niveau": "Avancé", 
            "duree": 12
        }
}
nom = etudiant["formation"]["nom"]
etudiant["formation"]["niveau"] = "Expert"
etudiant["formation"]["technologies"] = ["Python", "SQL", "Pandas", "MachineLearning"]
print(etudiant)