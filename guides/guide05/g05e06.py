"""
6.Definir una lista de 10 posiciones con
letras. Contar las vocales y mostrar el total.
"""


def vocals(array):
    counter = 0
    vocals = ['a', 'e', 'i', 'o', 'u']
    for letter in array:
        for vocal in vocals:
            if letter == vocal:
                counter += 1
    return counter


array = ['z', 'e', 'p', 'o', 'p', 'u', 'i', 's', 'a', 'd']
print(array)
print('There are', vocals(array), 'vocals.')
