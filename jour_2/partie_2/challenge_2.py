produit = {
 "nom": "Ordinateur", "prix": 8500,
 "stock": 12, "categorie":
"Informatique"
}


produit["prix"] = 7900
produit['marque'] = "Lenovo"
produit["disponible"] = True
del produit["stock"]
produit.pop("categorie")

print(produit)