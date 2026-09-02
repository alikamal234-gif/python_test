donnees = ["Omar", 25, "Casablanca", 15.5, True]

print("=====> types : \n")
for i in donnees:
    print(f"{i} : {type(i)}")
print("=====> nomber de chaque type \n")
compte = {}
for i in donnees :
    if type(i) in compte:
        compte[type(i)] += 1
    else :
        compte[type(i)] = 1

print(compte)

list_nombers = []
for i in donnees : 
    if type(i) == int or type(i) == float:
        list_nombers.append(i)

print(list_nombers)