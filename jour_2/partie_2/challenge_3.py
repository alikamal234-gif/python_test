notes = {"Python": 15, "SQL": 13, "JavaScript": 17, "Git": 14, "Linux": 12}
print(list(notes.keys()))
print(list(notes.values()))
print(list(notes.items()))

print(f"moyen : {max(list(notes.values())) / len(list(notes.values()))} , meilleur : {max(list(notes.values()))} , mauvaise : {min(list(notes.values()))}")