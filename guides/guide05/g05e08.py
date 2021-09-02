"""
8. Ingresar nombres , luego buscar un nombre y
de encontrarlo decir en qué posición está.
"""


def insertNames():
    names = []
    confirm = input('Do you like to input a name? y/n ')
    while confirm == 'y':
        names.append(input("What's the name? "))
        confirm = input('Do you like to input another name? y/n ')
    return names


def findName(names):
    name = input('What name would you like to find? ')
    for i in names:
        if name == i:
            return name, names.index(i)+1


names = insertNames()
place = findName(names)

print(place[0], "it's in", place[1])
