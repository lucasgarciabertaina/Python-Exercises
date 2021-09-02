"""
#1: Guardar en una lista los números pares
mayores que 0 y menores que 31. Los números no
se cargan a mano, ni por el usuario ni por el
programador, se generan por programa.
#2: Mostrar.
"""
condition = []
for number in range(2, 31, 2):
    condition.append(number)
print(condition)
