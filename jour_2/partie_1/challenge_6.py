L = [10, 20, 30, 40, 50]


def rechercheElement(item , list):
    for index , i in enumerate(list):
        if i == item : 
            return index
    return False
            

print(rechercheElement(40,L))