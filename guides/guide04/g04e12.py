"""
Mostrar el valor doble del número de dos cifras
(que es el único número) encontrado en la
cadena. Ej.: 'Juan tiene 25 años' mostraría
el número 50, ‘El dólar va a llegar este mes
a 57 pesos casi seguro’,  mostraría 114.
"""
text = input('Input a text with a number please: ')

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

decimal = []
position = 0
for i in completeText:
    for j in i:
        if 48 <= ord(j) <= 57:
            decimal.append(j)

for k in range(len(completeText)):
    if completeText[k] == decimal[0]+decimal[1]:
        position = k
        number = int(decimal[0]+decimal[1])


completeText[position] = str(number*2)

text = ''
for i in completeText:
    text += i
    text += ' '

print(text)
