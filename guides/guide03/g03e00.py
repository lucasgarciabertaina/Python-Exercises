"""
(4 de la guía 2) #1 Pedir el ingreso de 10
números. Contar los mayores de 23.
Almacenar los que cumplen la condición.
#2 Mostrar el resultado.
"""
condition = []
for i in range(10):
    number = float(input('Insert a number: '))
    if number > 23:
        condition.append(number)

print('The numbers greater than 23 are:', condition)
