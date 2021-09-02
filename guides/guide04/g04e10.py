""" 
En los siguientes ejercicios (6 a 11)
trabajamos con el texto: “Quiero comer manzanas
, solamente manzanas.”, 
considerar que una palabra es toda secuencia de
caracteres diferentes de los separadores 
(los caracteres separadores son el espacio,
la coma y el punto).

Determinar cuál es la vocal que aparece 
con mayor frecuencia.
"""
text = 'Quiero comer manzanas, solamente manzanas.'
withoutDot = text.split('.')
withoutCommaAndDot = withoutDot[0].split(',')


array = []
completeText = []
for i in withoutCommaAndDot:
    array.append(i)
    arrayElemets = array[0].split(' ')
    for j in arrayElemets:
        if j != '':
            completeText.append(j)
    array = [] 

a = 0
e = 0
i = 0
o = 0
u = 0

for k in completeText:
    for j in k:
        if j == 'a':
            a += 1
        elif j == 'e':
            e += 1
        elif j == 'i':
            i += 1
        elif j == 'o':
            o += 1
        elif j == 'u':
            u += 1


array = [a,e,i,o,u]
position = 0
times = 0
for i in range(len(array)):
    if i > times:
        position = i
        times = array[i]  

vocals = ['a','e','i','o','u']
print('The vocal',vocals[position],' repeted', times,'times')

        