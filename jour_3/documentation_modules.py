"""

math  :  Fonctions mathématiques de base et avancées (trigonométrie, logarithmes, constantes comme π et e).

datetime  :  Manipulation et gestion des dates, heures et grandeurs temporelles (durées, horodatage).

os  :  Interaction avec le système d'exploitation (chemins, répertoires, variables d'environnement).

glob  :  Recherche et filtrage de fichiers/dossiers correspondant à un motif (utilisant des caractères génériques/wildcards).

string  :  Opérations courantes et constantes prédéfinies sur les chaînes de caractères (ponctuation, chiffres, lettres).

random  :  Génération de nombres pseudo-aléatoires, tirages au sort et mélanges d'éléments.

csv  :  Lecture, écriture et structuration de données au format tabulaire CSV.

json  :   Encodage et décodage (sérialisation) de données au format standard JSON.

"""

import math , datetime , os , glob , string , random , csv , json 

#  math 


x = math.sqrt(64)
print(x) 
x = math.ceil(1.4)
print(x)
x = math.floor(x)
print(x)
x = math.pi
print(x)

# datetime

x = datetime.datetime.now().strftime("%A")
print(x)
x = datetime.datetime.now().year
print(x)
x = datetime.datetime.now()
print(x)
x = datetime.datetime(2020,5,17).strftime("%B")
print(x)

# os

print(os.listdir())
# os.mkdir("test")
# os.rmdir("test")
# os.path.join("test","test.txt")


# glob
print(glob.glob("partie_2/*.py"))
print(glob.glob("**/*.py"))
print(glob.glob("?.py"))
print(glob.glob("??.py"))


# string
print("\nstring \n")
print(string.ascii_letters)
print(string.ascii_lowercase)
print(string.ascii_uppercase)
print(string.digits)
print(string.whitespace)
print(string.capwords("aaa"))
print(string.punctuation)

#random 

print(random.randint(1, 10))
print(random.choice([1,2,3,4,5]))
print(random.choices([1,2,3,4,5]))
print(random.shuffle([2,4,8,9,2,3]))



# csv
with open("test.txt" , "r") as f:
    txt = csv.reader(f)
    print(list(txt))


with open("test.txt" , "r") as f:
    txt = csv.DictReader(f)
    print(list(txt))

with open("test.txt" , "a") as f:
    write = csv.writer(f)

    write.writerow(["\ntest" , "test" , "test"])




# json

user = {
    "name": "ali",
    "age": 22,
    "city": "youssoufia"
}
result = json.dumps(user)

print(user)
print(result)

data = '{"name": "Ali", "age": 22}'

user = json.loads(data)

print(user)

print(type(user) , type(result))