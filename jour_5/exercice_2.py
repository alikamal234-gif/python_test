class Voiture :
    def __init__(self , marque : str , modele : str , prix : int | float , kilometrage : int = 0):
        self.marque = marque
        self.modele = modele
        self.prix = prix
        self.kilometrage = kilometrage

    def afficher_info(self):
        return f"Marque: {self.marque}\nModèle: {self.modele}\nPrix: {self.prix}\nKilométrage: {self.kilometrage}"

class VoitureElectrique(Voiture):
    def __init__(self, marque, modele, prix, kilometrage , autonomie):
        super().__init__(marque, modele, prix, kilometrage)
        self.autonomie = autonomie
    def afficher_info(self):
        return f"Marque: {self.marque}\nModèle: {self.modele}\nPrix: {self.prix}\nKilométrage: {self.kilometrage}\nAutonomie: {self.autonomie} km"

class Concession:
    def __init__(self , nom):
        self.nom = nom
        self.inventaire = []
    def ajoute_voiture(self , voiture : Voiture | VoitureElectrique) :
        self.inventaire.append(voiture)

    def afficher_inventaire(self):
        for i in self.inventaire:
            return i.afficher_info()
    def vendre_voiture(self , marque , modele):
        for i in self.inventaire:
            if i.marque == marque and i.modele == modele :
                return f"La voiture {i.marque} a été vendue"
        return "La voiture n'a pas été trouvée"

    def calcul_prix(self):
        info = {
            "total_prix" : 0,
            "moyen_prix" : 0
        }
        for i in self.inventaire:
            info["total_prix"] += i.prix
        info["moyen_prix"] = info["total_prix"] / len(self.inventaire)
        return info

    def __str__(self):
        return f"le nom de la concession est {self.nom} est le nombre de voitures en inventaire est {len(self.inventaire)}"



concession = Concession("Concession de Centre")
voiture_1 = Voiture("marque 1" , "modele 1" , 100 , 200)
voiture_2 = Voiture("marque 2" , "modele 2" , 300 , 600)
voiture_3 = Voiture("marque 3" , "modele 3" , 300 , 900)
voiture_4 = VoitureElectrique("marque 4" , "modele 4" , 400 , 200 , 1000)
voiture_5 = VoitureElectrique("marque 5" , "modele 5" , 300 , 600 , 5000)
voiture_6 = VoitureElectrique("marque 6" , "modele 6" , 600 , 900 , 7000)


concession.ajoute_voiture(voiture_1)
concession.ajoute_voiture(voiture_2)
concession.ajoute_voiture(voiture_3)
concession.ajoute_voiture(voiture_4)
concession.ajoute_voiture(voiture_5)
concession.ajoute_voiture(voiture_6)

print(concession.afficher_inventaire())
print(concession.vendre_voiture("marque 3" , "modele 3"))
print(concession.vendre_voiture("marque 7" , "model 7"))

print(concession)
print(concession.calcul_prix())