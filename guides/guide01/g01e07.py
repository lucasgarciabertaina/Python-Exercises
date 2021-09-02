""" 
Pedir un nombre y una opción ('>' o '<') y según
esta mostrar por ejemplo.: Juan es menor de edad
"""

name = input('Ingrese el nombre: ')
option = input('Es < o >: ')

if option == '<':
    print(name, ' es menor de edad.')
elif option == '>':
    print(name, ' es mayor de edad.')
else:
    print('No ah ingresado ninguna de las opciones. Intentelo nuevamente.')
