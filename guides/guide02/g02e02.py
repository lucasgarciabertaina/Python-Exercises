""" 
Preguntar si hay datos para ingresar,
en caso afirmativo solicitar un número
entero y decir si es negativo o no.
Preguntar si repite.
"""
start = input('Is there data to enter? ')
while start != 'No':
    number = float(input('Enter a number: '))
    if number < 0:
        print(number, ' is negative')
        start = input('Is there data to enter? ')
    else:
        print(number, ' is positive')
        start = input('Is there data to enter? ')
