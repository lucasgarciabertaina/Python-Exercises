"""
#1: Pedir 12 números y guardarlos en una lista,
#2: luego recorrerla y almacenar el promedio en
la última posición. #3: Mostrar el promedio.
"""
numbers = []
total = 0

for i in range(12):
    number = int(input('Insert a number: '))
    numbers.append(number)

for i in range(12):
    if i != 11:
        total = total + numbers[i]
    else:
        total = total + numbers[i]
        average = total/12
        numbers.append(average)

print('The average of the 12 numbers is: ', numbers[-1])
