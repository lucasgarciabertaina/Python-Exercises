"""
Transformar la cadena "River vuelve
a las copas", en la cadena
"River vuelve a la copa".
Resolverlo recorriendo la cadena
original como si fuera una lista.
"""
strg = 'River  vuelve a las copas'
realStrg = ''
for i in strg:
    if i != 's':
        realStrg += i
print(realStrg)
