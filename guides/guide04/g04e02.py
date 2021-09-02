"""
Transformar la cadena "Curso de
Python" en la cadena "Curso de
Programación en Python".
Cortar la cadena original,
agregarle el literal
"Programación en" y concatenar.
"""

strg = 'Curso de Python'
array = strg.split(' ')
newStrg = ''
for i in range(len(array)):
    if i == 2:
        newStrg += 'Programación en '
        newStrg += array[i]
    else:
        newStrg += array[i]+' '
print(newStrg)
