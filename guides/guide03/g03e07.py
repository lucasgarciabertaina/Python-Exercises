""" 
#1: Ingresar nombres , luego #2: buscar un
nombre y de encontrarlo decir en qué posición
está.
"""
names = []
option = input('Do you want to enter names?  (yes/no)')
while option != 'no':
    name = input('Write a name: ')
    names.append(name)
    option = input('Do you want to enter names?  (yes/no)')


nameSearcher = 'Peter'

for i in range(len(names)):
    if names[i] == nameSearcher:
        print(nameSearcher, 'is in position', i)
