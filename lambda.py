people = [
    {"name": "Owido", "house": "Watari"},
    {"name": "Giddy", "house": "Rima"},
    {"name": "Tokunbo", "house": "Emotan"}
]

people.sort(key=lambda person: person["name"])

print(people)