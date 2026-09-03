

def types():
    errors_as_decs = {}
    with open("data/exercice.txt") as f :
        errors = f.readlines()
    for i in errors :
        index_start = i.find("[")
        index_fin = i.find("]")

        key = i[index_start+1:index_fin]
        if key in errors_as_decs:
            errors_as_decs[key] += 1
        else :
            errors_as_decs[key] = 1

    return errors_as_decs

def lists():
    errors_as_decs = {}
    with open("data/exercice.txt") as f :
        errors = f.readlines()
    for i in errors :
        index_start = i.find("[")
        index_fin = i.find("]")

        key = i[index_start+1:index_fin]
        value = i[index_fin+1:]
        if key in errors_as_decs :
            errors_as_decs[key].append(value)
        else :
            errors_as_decs[key] = [value]

    return errors_as_decs


def number_log():
    number_logs = types()
    resultat = ""
    with open("data/resume_logs.txt" , "w") as f :
        for key , value in number_logs.items():
            resultat += f"{key} : {value}\n"
        f.write(resultat)
        print("logs est crée sucess")



# print(types())
# print(lists())
print(number_log())

