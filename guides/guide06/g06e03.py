# 3) Validar una dirección de correo electrónico

from typing import Counter

print('banana.'.index('.'))


def conditions(mail):
    if mail.count('@') != 1 or mail.count('.') != 1:
        return True
    elif mail.index('@') == 0 or mail.index('@') == len(mail)-1 or mail.index('.') == len(mail)-1 or mail.index('.') < 3:
        return True
    elif mail.index('@') > mail.index('.') or mail.index('@')+1 == mail.index('.'):
        return True
    else:
        return False


email = input('Input a email please:\n')

while conditions(email):
    email = input('Email invalid!\nPlease insert a correct format: \n')
print('Correct')
