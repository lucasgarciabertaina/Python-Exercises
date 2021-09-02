# 4) input con opciones
# (Ejemplo: ‘Quiere ingresar datos (si/no)”?)

def inputOptions(text):
    array = text.split('(')
    word = ''
    options = []
    inp = input(text)
    for i in range(len(array[1])):
        if array[1][i] == '/' or array[1][i] == ')':
            options.append(word)
            word = ''
        else:
            word += array[1][i]
    for i in options:
        if i == inp:
            return i
    return inputOptions("This option doesn't exist. Please write one of the follow options.\n"+text)


# optionA = inputOptions('Do you want input any data? (yes/no)\n')
# optionB = inputOptions('Choise one option: (blue/red/white)\n')
# print(optionA, optionB)
