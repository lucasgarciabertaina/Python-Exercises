"""
Pedir nombres y sexo de personas y mostrar al
final el total de mujeres y el nombre de cada
una.
"""
famales = []

option = input('Do you like to input a name? (y/n)')

while option != 'n':

    name = input('Whats is your name? Answer:')
    genere = input('What is your genere? Answer')
    if genere == 'famale':
        famales.append(name)
    option = input('Do you like to input a new name? (y/n)')

print('There are', len(famales), ' womans:', famales)
