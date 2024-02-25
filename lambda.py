people = [
    {"name": "Owido", "house": "Watari"},
    {"name": "Giddy", "house": "Rima"},
    {"name": "Tokunbo", "house": "Emotan"}
]

def f(person):
    return person["name"]


people.sort(key=f)

print(people)