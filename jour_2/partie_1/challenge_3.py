notes = [12, 4, 14, 11, 18, 13, 7, 10, 5, 9, 15, 8, 14, 16]


print(notes)
print("avg : ",sum(notes) / len(notes))

super_moyen = []
for i in notes : 
    if i > sum(notes) / len(notes):
        super_moyen.append(i)
print("supérieures à la moyenne : ",super_moyen)


infer_moyen = []
for i in notes : 
    if i < sum(notes) / len(notes):
        infer_moyen.append(i)
print("inférieures à la moyenne : ",infer_moyen)


print("la meilleure note" , max(notes))
print("mauvaise note : ",min(notes))
count = 0
for i in notes : 
    if i >= 10 :
        count += 1 
print("le nombre de notes supérieures ou égales à 10 : " , count)

print("le pourcentage de réussite : ", sum(notes) / 100 , "%")