"""
#1: Cargar letras por teclado en una lista.
#2: Luego pedir una letra por pantalla y
#3: decir cuántas veces está
(recorriendo la lista).
"""
sentence = input('Write a sentence...  ')
letter = input('Enter a letter: ')
total = 0
for i in range(len(sentence)):
    if sentence[i] == letter:
        total = total+1

print('The letter ', letter, 'is', total, 'times in the sentence')
