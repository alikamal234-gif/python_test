list = []
resultat = ""
chaine = input("écrite un chaine de charachter : ")
for i in chaine:
    list += i
number = len(chaine) 
while True:
    resultat += list[number-1]
    number -= 1
    if number == 0:
        break
print(resultat)



