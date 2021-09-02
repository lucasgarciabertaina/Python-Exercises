"""
Recibir por teclado una cadena de
números e insertar un punto cada 3
dígitos como divisorio de miles.
Ej.  1234567890 debería devolver
1.234.567.890
"""
from typing import Counter


number = input('Insert a number: ')
counter = 0
invertNumber = ''


for i in range(len(number)-1,-1,-1):
    invertNumber += number[i]
    counter += 1
    if counter == 3 and i != 0:
        counter = 0
        invertNumber += '.'

realNumber = ''

for i in range(len(invertNumber)-1,-1,-1):
    realNumber += invertNumber[i]

print(realNumber)


