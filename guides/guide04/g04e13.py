""" 
Pedir el ingreso de un nombre completo en la
forma <nombre> <apellido> (ejemplo: Juan Pérez)
y mostrarlo invertido y con coma <apellido>,
<nombre> (ejemplo: Perez, Juan).
"""
completeName = input('Input a comlete name please: ')
array = completeName.split(' ')
invComName = ''
for i in range(len(array)-1, -1, -1):
    invComName += array[i]
    invComName += ' '
print(invComName)
