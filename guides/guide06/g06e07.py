# 7) input de strings
# (validar largo por mínimo y/o máximo)
from g06e04 import inputOptions


def comprobator(w, mi, ma):
    if mi != '' and ma != '':
        if mi > len(w) or len(w) > ma:
            return True
    elif mi != '':
        if mi > len(w):
            return True
    elif ma != '':
        if ma < len(w):
            return True
    else:
        return False


def largueStrings(min='', max=''):
    option = inputOptions('Would you like to add any words? (yes/no)\n')
    words = []
    if option == 'yes':
        word = input('Insert a word please:  ')
        if comprobator(word, min, max):
            print('The word does not have the required length')
        else:
            words.append(word)
        option = inputOptions('Would you like to add any words? (yes/no)\n')
    while option == 'yes':
        word = input('Insert a word please:  ')
        if comprobator(word, min, max):
            print('The word does not have the required length')
        else:
            words.append(word)
        option = inputOptions('Would you like to add any words? (yes/no)\n')
    if words != []:
        print(words)


largueStrings(min=5, max=8)
