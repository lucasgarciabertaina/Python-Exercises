# Dado un archivo de texto en formato CSV (valores separados por coma), realizar un
# programa que solicite un año entre 1980 y 1999 (ambos incluídos) y muestre los nombres
# de las personas nacidas en el verano (considerar que el verano de un año incluye a los
# nacidos desde el 21 de diciembre del año anterior).
# De preferencia (no es obligatorio), hacer una función que reciba una fecha y que devuelva
# algún valor que sirva para determinar si corresponde al verano del año pedido.
from datetime import date


def summer(fn, year):
    ye, month, day = fn.split('-')
    y = int(ye)
    m = int(month)
    d = int(day)
    if m == 11 and d >= 21 and y == year-1:
        return True
    elif m < 3 and y == year:
        return True
    elif m == 3 and d <= 20 and y == year:
        return True
    else:
        return False


def year8099(y, read):
    bornSummer = []
    for _ in read:
        data = read.readline()
        data = data.split(',')
        data[1] = data[1][0:-1]
        if data[1][0:4] == y or int(data[1][0:4]) == int(y)-1:
            if summer(data[1][0:10], int(y)):
                bornSummer.append(data[0])
    if bornSummer == []:
        print('Nobody was born in summer')
    else:
        for i in bornSummer:
            print(i)


readCsv = open('nacidos.csv', 'r')
inpYear = input()
year8099(inpYear, readCsv)
