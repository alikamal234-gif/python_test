list_1 = [1, 2, 3, 4, 5]

list_2 = [x**2 for x in list_1 ]

list_2.append(36)
assert len(list_1) == len(list_2) , "Attention les 2 listes n'ont pas la même taille"
