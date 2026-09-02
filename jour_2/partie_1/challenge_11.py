nombres = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


list_carre = [x**2 for x in nombres ]
print(list_carre)

list_pairs = [x for x in nombres if x % 2 == 0]
print(list_pairs)

list_cinq = [x for x in nombres if x > 5]
print(list_cinq)