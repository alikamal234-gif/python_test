number = int(input("écrite un nomber : "))

if number % 2 == 0 :

    resultat = number // 2
elif number % 2 != 0:
    resultat = number * 3 + 1 

print(resultat)