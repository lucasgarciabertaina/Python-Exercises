"""
Decir cuántas veces se repite una
letra cualquiera, en un texto dado.
Por recorrido.
"""

text = input('Input a sentence: ')
letter = input('Input a letter: ')
total = 0
for i in text:
    if i == letter:
        total += 1

print('The letter', letter, ' is repeated', total, ' times')
