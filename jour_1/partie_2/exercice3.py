number = int(input("écrite un nomber : "))
list =  []
mo = ""
while True:
    if number == 1:
        break
    elif number % 2 == 0 :
        number = number // 2
        list.append(number)
    elif number % 2 != 0:
        number = number * 3 + 1 
        list.append(number)
for i in list:
    mo += f"{i} , "


print(f"resultat est {number} => ({mo[:-3]})")