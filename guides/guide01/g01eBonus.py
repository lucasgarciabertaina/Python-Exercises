"""
Piedra papel o tijera
"""
from random import random

options = ['Piedra', 'Papel', 'Tijera']
option = random()
choose = input('Ingrese Piedra Papel o Tijera: ')

if option < 0.3:
    option = options[0]
elif option >= 0.33 or option < 0.66:
    option = options[1]
else:
    option = options[2]

if choose == option:
    print(option, 'and', choose, 'are the same')
elif choose == 'Piedra' and option == 'Papel':
    print('You lose! ', option, '>', choose)
elif choose == 'Papel' and option == 'Tijera':
    print('You lose!', option, '>', choose)
elif choose == 'Tijera' and option == 'Piedra':
    print('You lose!', option, '>', choose)
else:
    print('You win!', choose, '>', option)
