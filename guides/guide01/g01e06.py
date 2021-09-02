""" 
Leer dos números y luego una opción (puede ser 
'+' o '-'), y según la opción elegida realizar el cálculo.
"""
number1 = float(input('Ingrese el primer número: '))
number2 = float(input('Ingrese el segundo número: '))

operation = input('Escriba la operación + - :')


if operation == '+':
    add = number1+number2
    print(number1, ' + ', number2, ' = ', add)
elif operation == '-':
    substract = number1-number2
    print(number1, ' - ', number2, ' = ', substract)
else:
    print('No haz ingresado correctamente la operación')
