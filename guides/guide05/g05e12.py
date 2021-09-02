"""
12. Cargar en listas los nombres y fechas de
nacimiento de varias personas, luego recorrerlo
y mostrar los nombres de los mayores de edad.
Funciones de carga y cálculo de edad.
"""


def namesAndAges():
    names = []
    ages = []
    confrmation = input('Do you like to upload any data? y/n ')
    while confrmation == 'y':
        names.append(input("What's your name? "))
        ages.append(int(input("What's your age? ")))
        confrmation = input('Do you like to upload more data? y/n ')
    return names, ages


def ageing(names, ages):
    legalAge = []
    for i in range(len(ages)):
        if ages[i] >= 18:
            legalAge.append(names[i])
    return legalAge


data = namesAndAges()
names = data[0]
ages = data[1]

print("People who have more than 18 are", ageing(names, ages))
