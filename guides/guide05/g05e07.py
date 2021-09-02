"""
7. Almacenar en dos  listas paralelas, nombres
y sexos de 8 personas. Al finalizar, recorrerlas
y mostrar los nombres de las mujeres.
Dos funciones: carga y mostrarMujeres
"""


def charge(names, generes):
    for i in range(8):
        names.append(input("What's your name? "))
        generes.append(input("What's your genere? "))


def showWomans(names, generes):
    womens = []
    for i in range(len(generes)):
        if generes[i] == 'f':
            womens.append(names[i])
    return womens


names = []
generes = []
charge(names, generes)
print(showWomans(names, generes))
