""" 
En los siguientes ejercicios (6 a 11)
trabajamos con el texto: “Quiero comer manzanas
, solamente manzanas.”, 
considerar que una palabra es toda secuencia de
caracteres diferentes de los separadores 
(los caracteres separadores son el espacio,
la coma y el punto).

Contar la cantidad de letras
(no incluir los separadores).

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

counter = 0
for i in completeText:
    for j in i:
        counter += 1

print('There are',counter,' letters.')
