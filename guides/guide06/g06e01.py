# 1) Concatenar un número indeterminado de strings
# con un caracter determinado (por defecto un espacio)

def concatenation(*args, character=' '):
    text = ''
    for i in args:
        text += i
        text += character
    print(text)


# concatenation('a', 'b', 'c', 'd', 'e')
# concatenation('a', 'b', 'c', 'd', 'e', character='-')
