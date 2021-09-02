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

5. Averiguar qué cantidad de letras tiene la
palabra más larga. Para ello, primero cargar
cada palabra en una lista y luego obtener la
solicitada. Usar dos funciones.
"""


def stringToArray(string):
    string = string.lower()
    array = string.split(' ')
    exeptions = ['.', ',']
    condition = False
    for word in array:
        for letter in word:
            for exept in exeptions:
                if letter == exept:
                    condition = True
                    position = array.index(word)
                    realWord = array[position].replace(exept, '')
        if condition:
            array[position] = realWord
            condition = False

    return array


def wordMostLonger(array):
    counter = 0
    for word in array:
        if len(word) > counter:
            counter = len(word)
    return counter


if __name__ == "__main__":
    text = 'Quiero comer manzanas, solamente manzanas.'
    array = stringToArray(text)
    print(text)
    print('The word most longer have', wordMostLonger(array), 'letters.')
