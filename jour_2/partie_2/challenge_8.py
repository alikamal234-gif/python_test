ventes = [
 {"produit": "PC", "categorie": "Informatique", "prix": 8000, "quantite": 2},
 {"produit": "Souris", "categorie": "Accessoire", "prix": 150, "quantite": 10},
 {"produit": "Clavier", "categorie": "Accessoire", "prix": 300, "quantite": 5},
 {"produit": "PC", "categorie": "Informatique", "prix": 8000, "quantite": 1},
 {"produit": "Écran", "categorie": "Informatique", "prix": 2500, "quantite": 3}
]


total = len(ventes)
total_vendue = 0
ca = 0
plus_cher = 0
categories_infos = {}
chiffre_produits = {}
for i in ventes : 
    ca += i["prix"] * i["quantite"]
    total_vendue += i["quantite"]
    if plus_cher < i["prix"]:       
        plus_cher = i["prix"]
    if i["categorie"] in categories_infos:
        categories_infos[i["categorie"]] += 1
    else :
        categories_infos[i["categorie"]] = 1

    if i["produit"] in chiffre_produits:
        chiffre_produits[i["produit"]] += i["prix"] * i["quantite"]
    else :
        chiffre_produits[i["produit"]] = i["prix"] * i["quantite"]

print(f"Nombre total de ventes : {total}\nChiffre d'affaires (CA) total : {ca}\nProduit le plus cher : {plus_cher}\nQuantité totale vendue : {total_vendue}\nChiffre d'affaires par produit : {chiffre_produits}\nNombre de produits par catégorie : {categories_infos}")
