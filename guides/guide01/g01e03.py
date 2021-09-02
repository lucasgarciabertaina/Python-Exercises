""" Leer un número real y emitir una leyenda informando si es 
mayor o igual a cero o bien es negativo (son dos opciones). """

num = float(input('Ingrese número real: '))

if num == 0:
    print('El número real ingresado es igual a 0')
elif num < 0:
    print('El número ', num, ' ingresado es menor a 0')
