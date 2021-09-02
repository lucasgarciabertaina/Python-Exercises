""" 
En los siguientes ejercicios (6 a 11)
trabajamos con el texto: “Quiero comer manzanas
, solamente manzanas.”, 
considerar que una palabra es toda secuencia de
caracteres diferentes de los separadores 
(los caracteres separadores son el espacio,
la coma y el punto).
 
Averiguar qué cantidad de letras tiene la
palabra más larga y cual es.

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

position = 0
times = 0
for i in range(len(completeText)):
    if len(completeText[i]) > times:
        position = i

print('The word most longer is', completeText[position], 'with', len(
    completeText[position]), 'letters')
