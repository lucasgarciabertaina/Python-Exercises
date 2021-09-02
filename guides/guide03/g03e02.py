"""
#1: Guardar letras en una lista de 10
posiciones. #2: Contar las vocales.
#3: Mostrar el total.
"""
letters = ['l', 'o', 'k', 'z', 'd', 'a', 'u', 'q', 'o']
vowels = 0
for i in range(len(letters)):
    if letters[i] == 'a' or letters[i] == 'e' or letters[i] == 'i' or letters[i] == 'o' or letters[i] == 'u':
        vowels = vowels + 1

print('The number of vowels in the string is as follows', vowels)
