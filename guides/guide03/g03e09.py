"""
Cargar en dos listas paralelas nombres y
sueldos. Luego mostrar los nombres de las
personas que ganan más de $85000.
"""

names = ['Carl', 'Stuart', 'Camile', 'Sofia', 'Richard']
salarys = [85000, 85001, 7999, 86000, 1]
namesMore85000 = []

for iterator in range(len(salarys)):
    if salarys[iterator] > 85000:
        namesMore85000.append(names[iterator])

print('Individuals earning more than $85,000 are: ', namesMore85000)
