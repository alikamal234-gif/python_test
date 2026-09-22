import math

def charger_villes(chemin):
    with open(chemin , "r") as f:
        lines = f.readlines()
        tuples = []
    for i in lines :
        tuples.append(tuple(i.split()))
    for index , i in enumerate(tuples) : 
        x = ""
        if len(i) > 3:
            x = ' '.join(i[0:len(i) - 2]).replace("\"" , "")
            y = (x , i[-2] , i[-1])
            tuples[index] = y
    return tuples
    

# print(charger_villes("villes.txt"))

def distance(villeA, villeB):
    distance_1 = (float(villeA[1]),float(villeA[2]))
    distance_2 = (float(villeB[1]),float(villeB[2]))

    return math.dist(distance_1, distance_2)


# print(distance(("Paris",48.8567,2.3522),("Bordeaux",44.84,-0.58)))

def index_mini_distance(distances):

    index_min = 0
    min_distance = math.inf

    for i, d in enumerate(distances):
        if d < min_distance:
            min_distance = d
            index_min = i

    return index_min


def itineraire_greedy(villes):
    ville_initiale = villes[0]
    villes_visitees = [ville_initiale]
    trajet = [ville_initiale]
    ville_actuelle = ville_initiale
    while len(villes_visitees) < len(villes):
        villes_non_visitees = []
        distances = []
        for ville in villes:
            if ville not in villes_visitees:
                villes_non_visitees.append(ville)
                distances.append(distance(ville_actuelle, ville))
        index = index_mini_distance(distances)
        ville_prochaine = villes_non_visitees[index]
        trajet.append(ville_prochaine)
        villes_visitees.append(ville_prochaine)
        ville_actuelle = ville_prochaine
    return trajet


def afficher_trajet(trajet):
    for i, ville in enumerate(trajet):
        if i < len(trajet) - 1:
            print(f"{ville[0]} -> ")
        else:
            print(ville[0])


# villes = charger_villes("mini_villes.txt")

# trajet = itineraire_greedy(villes)

# afficher_trajet(trajet)


def distance_totale(itineraire):
    total = 0
    for i in range(len(itineraire) - 1):
        total += distance(itineraire[i] , itineraire[i+1])
    return total


# print(distance_totale(itineraire_greedy(charger_villes("mini_villes.txt"))))


def analyse_resumer():
    total = len(charger_villes("mini_villes.txt"))
    villes = charger_villes("mini_villes.txt")
    trajet = afficher_trajet(itineraire_greedy(villes))
    distance_total = distance_totale(itineraire_greedy(charger_villes("mini_villes.txt")))
    print(total)
    print(trajet)
    print(distance_total)


analyse_resumer()