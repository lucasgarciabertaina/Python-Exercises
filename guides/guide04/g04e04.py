"""
Pasar una palabra a mayúsculas
cambiando los caracteres uno por uno
usando la tabla ASCII de referencia
(googlear la tabla y las funciones
de conversión en Python).
"""
majuscule = []
for i in range(65, 91):
    majuscule.append(i)

minuscule = []
for i in range(97, 123):
    minuscule.append(i)

word = input('Insert a word: ')
newWord = ''
for i in word:
    number = ord(i)
    for j in range(len(minuscule)):
        if minuscule[j] == number:
            number = majuscule[j]
            letter = chr(number)
            newWord += letter

print(newWord)
