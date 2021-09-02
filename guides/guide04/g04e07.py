""" 
Buscar una palabra y reemplazarla por otra
todas las veces que aparezca.
Ej.: ‘peras’ en lugar de ‘manzanas’
quedaría 'Quiero comer peras, solamente peras.' Sin usar replace.
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

word = input('What word would you like to use to replace apple?')
textChange = ''
for i in completeText:
    if i != 'manzanas':
        textChange += i
    else:
        textChange += word
    textChange += ' '

print(textChange)
