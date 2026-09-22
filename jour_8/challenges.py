import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def challenge1():
    data = pd.read_csv("c:/Users/Youcode/Desktop/python_test/jour_8/data/temperature.csv")
    y = data["temperature"].tolist()
    x = data["jour"].tolist()
    plt.plot(x , y)
    plt.title("l'evolution de la température pendant le semaine")
    plt.xlabel("jours")
    plt.ylabel("temperatures")
    plt.grid(True)
    plt.show()

def challenge2():
    data = pd.read_csv("c:/Users/Youcode/Desktop/python_test/jour_8/data/ventes_villes.csv")
    print(data)
    x = data["ville"].tolist()
    y = data["ventes"].tolist()
    plt.figure(figsize=(10,5))
    plt.bar(x,y)
    plt.title("les ventes par ville")
    plt.xlabel("villes")
    plt.ylabel("ventes")
    plt.grid(True)
    plt.show()

    # casablanca

def challenge3():
    data = pd.read_csv("c:/Users/Youcode/Desktop/python_test/jour_8/data/notes_etudiants.csv")
    plt.hist(data["note"],bins=len(data["note"]))
    plt.title("notes")
    plt.xlabel("notes")
    plt.ylabel("frequence")
    plt.grid(True)
    plt.show()

def challenge4():
    data = pd.read_csv("c:/Users/Youcode/Desktop/python_test/jour_8/data/heures_etude.csv")

    plt.scatter(data["heures_etude"] , data["note"])
    plt.title("relation entre heures et note")
    plt.xlabel("heures etude")
    plt.ylabel("notes")
    plt.grid(True)
    plt.show()


def challenge5():
    data = pd.read_csv("c:/Users/Youcode/Desktop/python_test/jour_8/data/entreprise.csv")
    moyennes = data.groupby("departement")["salaire"].mean()
    # plt.subplot(2,2,1)
    # plt.bar(data["employe"] , data["salaire"])
    # plt.subplot(2,2,2)
    # plt.hist(data["salaire"])
    # plt.subplot(2,2,3)
    # plt.scatter(data["experience"] , data["performance"])
    # plt.subplot(2,2,4)
    # plt.bar(moyennes.index , moyennes.values)
    # plt.show()

    fig , axe = plt.subplots(2,2)
    axe[0,0].bar(data["employe"] , data["salaire"])
    axe[0, 0].set_facecolor("lightblue")
    axe[0,1].hist(data["salaire"])
    axe[0, 1].set_facecolor("red")
    axe[1,0].scatter(data["experience"] , data["performance"])
    axe[1,0].set_facecolor("yellow")
    axe[1,1].bar(moyennes.index , moyennes.values)
    fig.suptitle("analyze")
    plt.show()


def challenge6():
    data = pd.read_csv(
        "c:/Users/Youcode/Desktop/python_test/jour_8/data/clients.csv"
    )
    fig, axe = plt.subplots(2, 2, figsize=(12, 8))
    sns.histplot(
        data=data,
        x="age",
        ax=axe[0, 0]
    )
    axe[0, 0].set_title("distribution de l'age")
    axe[0, 0].set_xlabel("age")
    axe[0, 0].set_ylabel("nombre")
    sns.countplot(
        data=data,
        x="ville",
        ax=axe[0, 1]
    )
    axe[0, 1].set_title("nombre de clients par ville")
    sns.boxplot(
        data=data,
        y="salaire",
        ax=axe[1, 0]
    )
    axe[1, 0].set_title("distribution des salaires")
    axe[1, 0].set_xlabel("")
    sns.barplot(data=data,x="sexe",y="salaire",ax=axe[1, 1])
    axe[1, 1].set_title("comparaison des salaires selon le sexe")

    plt.show()

def challenge7():
    data = pd.read_csv("c:/Users/Youcode/Desktop/python_test/jour_8/data/clients_depenses.csv")
    # sns.scatterplot(data , x="salaire" , y="depenses")
    # plt.show()
    # sns.scatterplot(data , x="nombre_commandes" , y="depenses")
    # plt.show()
    # sns.scatterplot(data , x="age" , y="salaire")
    sns.regplot(data=data , x="age" , y="salaire")
    plt.show()

# challenge7()


