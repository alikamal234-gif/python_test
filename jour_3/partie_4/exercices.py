# exercice 1
import math , datetime , os , glob

def exercice1():
    return f"l'hypoténuse d'un triangle rectangle dont les côtés sont 6 et 8 : {math.hypot(6,8)}"


def exercice2():
    liste1 = ["15/08/2025", "20/08/2023", "08/02/2017", "23/04/2009"]
    liste2 = ["2025-03-18", "2022-04-23", "2019-06-12", "2008-01-10"]

    liste2 = [x.replace("-" , "/") for x in liste2]
    date_list2 = [datetime.datetime.strptime(x , "%Y/%m/%d") for x in liste2]
    date_list2 = [x.strftime("%d/%m/%Y") for x in date_list2]
    date_list2 = [datetime.datetime.strptime(x , "%d/%m/%Y") for x in date_list2]
    date_list1 = [datetime.datetime.strptime(x , "%d/%m/%Y") for x in liste1]
    resultat = [f"{x} - {date_list2[index]} = {(x - date_list2[index])}" for index , x in enumerate(date_list1)]
    return [x.split(",")[0] for x in resultat]


def exercice3():
    PATH="dossier"
    obj = {}
    if PATH not in os.listdir() :
        os.mkdir(PATH)
        for i in range(3):
            with open(f"dossier/ficher_{i+1}.txt" , "w") as f:
                f.write(f"ficher {i+1}")

    path = glob.glob("dossier/*.txt")
    for i in range(3) :
        with open(path[i] , "r") as f :
            obj[path[i]] = f.read()

    return obj

def exercice4():
    PATH = "dossier"
    obj = {}
    path = glob.glob(f"{PATH}/*.txt")
    for i in path :
        with open(f"{i}" , "r") as f:
            obj[i] = f.readlines()

    return obj


# def Template() :


# rapport_template = Template("""Rapport d'analyse :- Projet : $projet- Date : $dateRésultats obtenus : $resultatsMerci pour votre confiance.""")
# rapport = rapport_template.substitute( projet="Prédiction des ventes", resultats="Précision du modèle : 92%")
# print(rapport)




def exercice5():
    



# print(exercice1())
# print(exercice2())
# print(exercice3())
# print(exercice4())