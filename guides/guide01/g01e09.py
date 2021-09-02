""" 
Realizar un algoritmo que permita ingresar un dato
numérico y determinar si es un número positivo de dos dígitos.
"""
number = float(input('Ingrese el número: '))

if number >= 10 and number < 100:
    print(number, ' Es un número positivo de dos digitos')
else:
    print(number, ' NO Es un número positivo de dos digitos')
