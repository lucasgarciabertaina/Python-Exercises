"""
13. Pedir el ingreso de un nombre completo
(Juan Pérez) y mostrarlo invertido y con coma
(Pérez, Juan).
"""

from g05e05 import stringToArray


def formalName():
    fullName = input('Please, insert your full name: ')
    array = stringToArray(fullName)
    print(array[1].capitalize(), ',', array[0].capitalize())


formalName()
