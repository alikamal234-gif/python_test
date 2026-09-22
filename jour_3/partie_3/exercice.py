def compute_list_sum(numbers = []):
    """this function for calcul sum of numbers pair 
        type is integer and float

        exemple : 
            >> print("resultat : " , compute_list_sum([1, 2, 3, 4, 5]))
            resulatat : 6
    """
    try : 
        resultat = 0
        for i in numbers :
            if i % 2 == 0:
                resultat += i
        return resultat
    except ValueError as v : 
        print("Le paramètre doit être un nombre")



print("resultat : ",compute_list_sum([1, 2, 3, 4, 5]))
print(compute_list_sum.__doc__)