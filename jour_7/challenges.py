import pandas as pd
import numpy as np
data = pd.read_csv("c:/Users/Youcode/Desktop/python_test/jour_7/data/clients.csv")
data2 = pd.read_csv("c:/Users/Youcode/Desktop/python_test/jour_7/data/clients_dirty.csv")
data3 = pd.read_csv("c:/Users/Youcode/Desktop/python_test/jour_7/data/ventes.csv")
data4 = pd.read_csv("c:/Users/Youcode/Desktop/python_test/jour_7/data/employes.csv")
def challenge1():
    print(data.head())
    print(data.tail())
    print(data.shape[1])
    print(data.shape[0])
    print(data.columns)
    print(data.index)
    print(data.dtypes)
    print(data.info())
    print(data.describe())
    print(data.select_dtypes(include=["number"]).columns.tolist())
    print(data["ville"].unique().tolist())
    print(len(data["ville"].unique().tolist()))
    print(data.groupby("ville")["client_id"].count())
    data.iloc[1,1] = np.nan
    print(data.isna().sum())


def challenge2():
    noms = data["nom"]
    noms_ages_villes = data[["nom","age","ville"]]
    print(noms_ages_villes.iloc[0:3,:])
    print(noms_ages_villes[noms_ages_villes["age"] > 30])
    print(data[data["salaire"] > 6000])
    print(data[data["ville"].str.lower() == "casablanca".lower()])
    print(data[(data["sexe"].str.lower() == "f") & (data["age"] > 30)])
    print(data[(data["ville"].str.lower() == "rabat") | (data["ville"].str.lower() == "casablanca")])
    print(data["ville"].isin(["Casablanca" , "Rabat"]))
    print(data[data["age"].between(25,35)])
    print(data[~(data["ville"] == "Casablanca")])
    print(data.loc[0 ,"age"])
    print(data.iloc[0 , 0])

def challenge3():
    print("la somme de nan : " ,data2.isna().sum())
    print("la some de data duplaquer : " , data2.duplicated().sum())
    print(data2.info())

    print(data2[data2.duplicated()])
    print(data2.drop_duplicates())
    print(data2[data2.duplicated()])

    data2["nom"].str.strip()
    data2["ville"].str.strip()

    print(data2["ville"].str.lower().str.strip())
    data2["age"] = data2["age"].fillna(data2["age"].mean())
    data2["age"] = data2["age"].astype(int)
    data2["salaire"]=data2["salaire"].str.replace('DH','').str.strip().astype(int)
    salaire_nega = data2[data2["salaire"] < 0]
    data2['date_inscription'] = pd.to_datetime(data2['date_inscription'])

    print(data2.info())
    print(data2.shape)
    print(data2)
    



def challenge4():
    chiffre_affaires = data3["prix"] * data3["quantite"]
    print(chiffre_affaires)
    data3["prix_avec_tva"] = data3["prix"] * 0.20
    def categoriser_prix(data):
        total = data["prix"] * data["quantite"]
        if total < 1000:
            return "Faible"
        elif 1000 <= total < 5000:
            return "Moyen"
        else:
            return "eleve"
    data3["categorie_prix"] = data3.apply(categoriser_prix , axis=1)
    print(data3)


def challenge5():
    data3["chiffre_affaires"] = data3["prix"] * data3["quantite"]
    print(data3["chiffre_affaires"].info())
    print(data3.groupby("ville")["chiffre_affaires"].sum())
    print(data3.groupby("ville")["chiffre_affaires"].mean())
    print(data3.groupby("ville")["chiffre_affaires"].count())
    print(data3.groupby("produit").count())
    print(data3.groupby("produit")["chiffre_affaires"].sum())
    print(data3.groupby("produit")["chiffre_affaires"].sum().max())
    print(data3.groupby("produit").agg({
        "prix" : ["mean" , "sum" , "min" , "max" , "count"],
        "quantite" : ["mean" , "sum" , "min" , "max" , "count"]
    }))


def challenge6():
    print(data3.groupby("departement")["salaire"].mean())
    data3["salaire_moyen_departement"] = data3.groupby("departement")["salaire"].transform("mean")
    data3["ecart_au_salaire_moyen"] = data3["salaire"] - data3["salaire_moyen_departement"]
    print(data3.groupby("departement")["performance"].mean())
    data3["performance_moyenne_departement"] = data3.groupby("departement")["performance"].transform("mean")
    print(data3[data3["salaire"] > data3["salaire_moyen_departement"]])
    print(data3.groupby("departement").agg({
        "salaire": ["mean", "sum", "min", "max", "count"],
        "performance": ["mean", "sum", "min", "max", "count"]
    }))
    print(data3.apply(
        lambda data: data["salaire"] * data["performance"],
        axis=1
    ))
    data3["score_salaire_performance"] = data3.apply(
        lambda data: data["salaire"] * data["performance"],
        axis=1
    )
    print(data3)
challenge6()




