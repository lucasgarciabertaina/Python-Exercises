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

1. Cuántas veces se repite una letra cualquiera
pedida. Parámetros: letra, cadena.
"""


def howMany(letter, string):
    counter = 0
    for i in string:
        if i == letter:
            counter += 1
    return(counter)


text = 'Quiero comer manzanas, solamente manzanas.'
letter = input('Insert a letter: ')
print('The letter', letter, 'is in', howMany(letter, text), ' times.')
