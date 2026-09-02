fruits = ["Pomme", "Banane", "Orange", "Fraise", "Mangue", "Kiwi"]


# A
print(fruits)
print(fruits[0])
print(fruits[-1])
print(fruits[2])

# B
print(fruits[0:3])
print(fruits[-3:])
print(fruits[::2])
# C

for index , i  in enumerate(fruits):
    if i.lower() == "orange":
        fruits[index] = "Ananas"
print(fruits)