# 5) creador de menúes
from g06e04 import inputOptions


def sayHi():
    print('Hi\n')


def sayGoodLuck():
    print('Good Luck!\n')


def closeAll():
    print('You believed it\n')


def menu(**kwargs):
    counter = 1
    print('=====MENU====\n')
    keys = ['hi']
    options = '('
    for key, value in kwargs.items():
        print(counter, ')', value)
        options += str(counter)
        options += '/'
        counter += 1
        keys.append(key)
    print(len(kwargs)+1, ') Close menú')
    options += str(counter)
    options += ')'
    option = inputOptions(options)
    for k in range(len(keys)):
        if str(k) == option:
            print('hi')
            eval(keys[k]+'()')
            return menu(**kwargs)


# menu(sayHi='Say hi to everyone!', sayGoodLuck='Say good luck to everyone!',
#      closeAll='Close the aplication')
# menu(sayHi='Say hi to everyone!', sayGoodLuck='Say good luck to everyone!',)
