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

4. Contar la cantidad de palabras.
"""


def counterWords(text):
    words = text.split(' ')
    return len(words)


text = 'Quiero comer manzanas, solamente manzanas.'

print(text)
print('There are', counterWords(text), 'words in a phrase.')
