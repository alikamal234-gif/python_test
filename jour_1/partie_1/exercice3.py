age = int(input("quelle est ton age : ")
)
if age <= 18 :
    print("l'entrée est refusé")
elif age > 18 and  age <= 25 :
    print("l'entrée est gratuite")
else :
    is_active = True
    while  is_active:
        member = input("tu a member dans ce club (yes / no)")
        if member.lower() == "yes":
            print("l'entrée est autorisée")
            is_active = False
        elif member.lower() == "no":
            print("l'entrée n'est pas autorisée")
            is_active = False
        else :
            print("essayer un autre fois")
            is_active = True