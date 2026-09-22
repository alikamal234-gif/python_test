import numpy as np


# niveau 1

def challenge1():
    list = np.array([28273, 27392 , 823829 , 183918 , 9245])
    print("type de tableau : " , type(list))
    print(np.shape(list)) #(5,)
    print(list.dtype) # int64
    print(np.ndim(list)) # 1
    print(np.size(list)) # 5
    print(np.min(list)) # 9245
    print(np.max(list)) # 823829
    print(np.mean(list)) # 214531.4
    print(list[0])
    print(list[-1])
    print(np.ndim([[[1,2,3] , [3,5,6]] , [[3,5,6] , [3,7,1]]])) # 3



def challenge2():
    jours = np.arange(10 , 20 , 2)
    temperature = np.linspace(10 , 40 , 5)
    prix = np.zeros(5)
    id_produits = np.full((5,) , 8)
    print(jours.dtype)
    print(temperature.dtype)
    print(prix.dtype)
    print(id_produits.dtype)
    

def challenge3():
    notes = np.array([[12 , 18 , 11],[9 , 20 , 7],[18 , 19 , 20]])
    print(f"les moyens c'est : {np.mean(notes , axis=1)}")
    print(f"les meilleures notes c'est : {np.max(notes , axis=1)}")
    print(f"les faibles notes c'est : {np.min(notes , axis=1)}")
    print(f"l'ecarts entres les notes  : {np.max(notes , axis=1) - np.min(notes , axis=1)}")
    print(f"etudiants obtenu notes superieure a la moyenne : \n{notes > np.mean(notes)}")


def challenge4():
    clients = np.array([[19 , 1200 , 20 , 1000] , [20 , 1300 , 25 , 1030] , [21 , 1900 , 30 , 2000]])
    print(clients[0])
    print(clients[: , 0])
    print(clients[0:2])
    print(np.shape(clients))
    print(len(clients))


def challenge5():
    clients = np.array([[19 , 1200 , 20 , 1000] , [20 , 1300 , 25 , 1030] , [21 , 1900 , 30 , 2000]])
    clients[0,0] = 20
    clients[: , 1] = np.zeros(3)
    clients_copy = np.copy(clients)
    clients[0,0] = 299
    print(clients_copy)
    print(clients)


#niveau 2

def challenge6():
    ventes = np.array([1000, 1500, 800, 2000, 1200])
    remises = np.array([10, 5, 0, 15, 10])
    qtt = np.array([3 , 6 , 7 , 10 , 200])
    tva = 20
    print("le chiffre d'affaires : " , ventes * remises * qtt / 100)
    print("CA avec tva : " , (ventes * (ventes - remises)) * np.sum(1 , tva/100))
    print("nombre de ventes" , len(ventes))
    print("la vent moyenne" , np.mean(ventes))
    print(f"minimale : {np.min(ventes)} , maximale : {np.max(ventes)}")


def challenge7():
    salaires = np.array([3200, 4500, 2800, 5100, 3900, 6200, 3500, 4700])
    print(np.mean(salaires))
    print(np.median(salaires))
    print(np.var(salaires))
    print(np.std(salaires))
    print(np.percentile(salaires , 75))
    print(np.min(salaires))
    print(np.max(salaires))

def challenge8():
    temperature = np.array([10 , 20 , 40 , 30 , 45])
    print(np.mean(temperature))
    print(f"jour plus chaude jour : {np.argmax(temperature) + 1}\njour plus froid est : {np.argmin(temperature) +1}")
    print(f"temperature superieure a la moyenne sont : {temperature[temperature > np.mean(temperature)]}")
    print(np.diff(temperature))



def challenge9():
    ventes = np.array([[10 , 388 , 28] , [119 , 38 , 24] , [19 , 448 , 208]])
    print(np.sum(ventes , axis=0))
    print(np.mean(ventes , axis=0))
    print(np.sum(ventes , axis=1))
    print(np.mean(ventes , axis=1))
    print(np.argmax(np.sum(ventes , axis=0) , axis=0))
    print(np.argmax(np.sum(ventes , axis=1)))


def challenge10():
    clients = np.array([[19 , 2000 , 20 , 200] , [40 , 999 , 15 , 100] , [31 , 3000 , 21 , 322]])
    print(clients[(clients[: , 0] > 30) & (clients[: , 1] > 1000)])
    print(clients[(clients[: , 0] > 30) | (clients[: , 1] > 1000)])
    print(len(clients[(clients[: , 0] > 30) & (clients[: , 1] > 1000)]))


# niveau 3

def challenge11():
    mesures = np.array([1,2,-100,3,4,5,200])
    iqr = np.percentile(mesures , 75) - np.percentile(mesures , 25)
    lower = np.percentile(mesures , 25) - 1.5 * iqr
    upper = np.percentile(mesures , 75) + 1.5 * iqr
    print(np.argwhere((mesures < lower) | (mesures > upper)))


def challenge12():
    dataset = np.array([1 , 3 , 5 , np.nan , 7 , np.nan])
    print(np.where(np.isnan(dataset)))
    print(len(np.argwhere(np.isnan(dataset))))
    dataset[np.where(np.isnan(dataset))] = np.nanmean(dataset)
    print(dataset)

def challenge13():
    scores = np.array([
        15, 18, -5, 12, 105,
        np.nan, 17, 20, -2, 150,
        14, np.nan, 19, 8, 120
    ])
    score_clean  = scores[(~np.isnan(scores)) & (scores > 0)]
    iqr = np.percentile(score_clean , 75) - np.percentile(score_clean , 25)
    lower = np.percentile(score_clean , 25) - 1.5 * iqr
    upper = np.percentile(score_clean , 75) + 1.5 * iqr
    print(score_clean[(score_clean > lower) & (score_clean < upper)])


def challenge14():
    users = np.array(["ali" , "moussa" , "youssef" , "kadiri" , "ilyas"])
    scores = np.array([10 , 20 , 20 , np.nan , 30])
    score_sorted = np.sort(scores)
    index_croissant = np.argsort(scores)
    print(users[index_croissant])
    print("meilleurs 3 notes : ", score_sorted[-4:-1] )
    print("pires 3 notes : ", score_sorted[ 0: 3] )
    print(np.unique(scores))



def challenge15():
    notes = np.array([
        [12, 15, 14],
        [18, 16, 17],
        [9, 11, 10],
        [14, 13, 15]
    ])

    print("dimensions : ", np.shape(notes))

    moyenne_matieres = np.mean(notes, axis=0)
    print("moyenne par matière : ", moyenne_matieres)

    moyenne_etudiants = np.mean(notes, axis=1)
    print("moyenne par étudiant : ", moyenne_etudiants)

    print("note minimale : ", np.min(notes))
    print("note maximale : ", np.max(notes))
    moyenne = np.mean(notes)
    print("moyenne générale : ", moyenne)
    print("étudiants au-dessus de la moyenne : ",
          moyenne_etudiants[moyenne_etudiants > moyenne])
    classement = np.argsort(moyenne_etudiants)[::-1]
    print("classement : ", classement)
    print("valeurs uniques : ", np.unique(notes))
    print("anomalies : ", notes[notes < 10])
    print("ecart-type : ", np.std(notes))



def challenge20():
    arra = np.array([[19,1000,20] , [20,1200,30] , [23,2000,40] , [30,5000,90]])
    min = np.min(arra , axis=0)
    max = np.max(arra , axis=0)
    mean = np.mean(arra , axis=0)
    std = np.std(arra , axis=0)
    
    standardisation = (arra - mean) / std
    normalisation = (arra - min) / (max - min)
    print(standardisation)
    print(normalisation)
    print(np.mean(standardisation))
    print(np.std(standardisation))





def challenge21():
    arr1 = np.array([100 , 200 , 400])
    arr2 = np.array([300 , 299 , 322])

    print(arr1 + arr2)
    print(arr1 - arr2)
    print(arr1 * arr2)
    print(arr1 / arr2)

def challenge22():
    clients = np.array([
        [20, 1000, 200],
        [22, 1200, 250],
        [35, 3000, 500],
        [21, 1100, 220],
        [40, 5000, 800]
    ])
    client_initial = clients[0]
    distance = np.sqrt(np.sum((client_initial - clients) ** 2 , axis=1))
    print(distance)
    print(clients[np.argmin(distance)])
    print(clients[np.argmax(distance)])



def challenge23():
    vecteurs = np.array([
        [1, 2, 3],
        [2, 4, 6],
        [3, 1, 1],
        [1, 2, 2]
    ])
    # simil



