"""
Pedir el ingreso de 10 números. Contar los
mayores de 23. Mostrar el resultado.
"""
i = 0
j = 0
numbers = []
while i != 10:
    number = float(input('Enter a number: '))
    if number > 23:
        j = j+1
        numbers.append(number)
    i = i+1
print('The numbers greater than 23 are: ', j)
print(numbers)
