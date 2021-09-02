""" 
Leer dos números reales y
mostrarlos en orden creciente
"""
number1 = float(input('Ingrese el primer número: '))
number2 = float(input('Ingrese el segundo número: '))

if number1 > number2:
    print('[', number1, ',', number2, ']')
elif number1 < number2:
    print('[', number2, ',', number1, ']')
