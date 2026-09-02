L = [7, 23, 5, 23, 7, 19, 23, 12, 29, 7, 5]


def counter(list):
    depluquer = {}
    for i in list : 
        if i in depluquer :
            depluquer[i] += 1
        else :
            depluquer[i] = 1
    return depluquer


print(counter(L))

