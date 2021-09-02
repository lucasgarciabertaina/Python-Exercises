""" Leer dos números y 
decir cuál es el mayor. """

number1 = float(input('Ingrese la primera nota: '))
number2 = float(input('Ingrese la segunda nota: '))

if number1 > number2:
    print(number1, ' > ', number2)
elif number1 < number2:
    print(number2, ' > ', number1)
else:
    print(number2, ' > ', number1)
