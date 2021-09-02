"""
Los siguientes ejercicios son en su mayoría
para reutilizar los enunciados de guías
anteriores, aplicando en la solución el uso de
funciones.
En los primeros 5 ejercicios trabajamos con el
texto: “Quiero comer manzanas, solamente
manzanas.”, considerar que una palabra es
toda secuencia de caracteres diferentes de los
separadores (los caracteres separadores son el
espacio, la coma y el punto).

2. Buscar una palabra y reemplazarla por otra
todas las veces que aparezca.
Ej.: ‘peras’ en lugar de ‘manzanas’ quedaría
'Quiero comer peras, solamente peras.'
"""


def stringToArray(string):
    string = string.lower()
    arrayWithoutDot = string.split('.')
    arrayWithoutSpace = arrayWithoutDot[0].split(' ')
    array = []
    for i in range(len(arrayWithoutSpace)):
        if i == 2:
            array.append(arrayWithoutSpace[i][0:8])
        else:
            array.append(arrayWithoutSpace[i])
    return array


def arrayToString(array):
    string = ''
    for i in range(len(array)):
        if i == 2:
            string += array[i]+', '
        elif i == len(array)-1:
            string += array[i]+'.'
        else:
            string += array[i]+' '
    string = string.capitalize()
    return(string)


def replaceWord(array, palabraARemplazar, palabra):
    for i in range(len(array)):
        if array[i] == palabraARemplazar:
            array[i] = palabra
    return array


text = 'Quiero comer manzanas, solamente manzanas.'

print(text)
wordToReplace = input('What word do you like to replace? ')
word = input('By what word? ')
array = replaceWord(stringToArray(text), wordToReplace, word)
print(arrayToString(array))
