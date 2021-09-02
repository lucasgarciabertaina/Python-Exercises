"""
Pedir dos nombres y edades respectivas y luego
construir una sola cadena con un texto que
muestre el nombre del mayor y cuanto le lleva
al menor.
(Ejemplo:  entrada -> 'Juan' 30 'Pedro' 23 /
 salida -> 'Juan le lleva 7 años a Pedro')
"""
name0 = input('Input the first name: ')
age0 = int(input('Input your age: '))
name1 = input('Input the second name: ')
age1 = int(input('Input your age: '))
array = []
if age0 > age1:
    array.append(name0)
    array.append(age0-age1)
    array.append(name1)
else:
    array.append(name1)
    array.append(age1-age0)
    array.append(name0)


print(array[0], 'le lleva', array[1], 'años a ', array[2])
