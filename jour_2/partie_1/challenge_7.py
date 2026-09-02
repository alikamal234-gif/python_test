L = [7, 23, 5, 23, 7, 19, 23, 12, 29]


def compterOccurrences(item , list):
    count = 0
    for i in list :
        if i == item :
            count += 1
    return count

print(compterOccurrences(23, L)) 
print(compterOccurrences(7, L)) 
print(compterOccurrences(100, L))