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

3. Contar la cantidad de letras (mayúsculas, 
minúsculas, acentuadas, eñes).
"""


def counterLetters(text):
    exeptions = [';', ',', ' ', ':', '.']
    counter = 0
    condition = True
    for i in text:
        for j in exeptions:
            if i == j:
                condition = False
        if condition:
            counter += 1
        else:
            condition = True
    return counter


text = 'Quiero comer manzanas, solamente manzanas.'

print(text)
print('There are', counterLetters(text), 'letters in a phrase')
