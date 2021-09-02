"""
Mostrar por pantalla una lista de
20 números enteros consecutivos, 
comenzando con un número 
ingresado por teclado.
"""
number = int(input('Enter a number: '))
i = 1
while i != 20:
    print('Number ', number)
    i += 1
    number = number+1
