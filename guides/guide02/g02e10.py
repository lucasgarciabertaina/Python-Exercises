"""
Dada una lista de nombres y de salarios
respectivos, determinar el salario mínimo y
mostrar el nombre de la persona que menos gana.
"""

salarys = ['Juan', 50, 'Pedro', 80, 'Lorenzo', 96, 'Carlitos', 5]
minime = ''
for salary in range(0, len(salarys), 1):
    if salary % 2 != 0:
        if minime == '' or salarys[salary] < minime:
            minime = salarys[salary]
            person = salarys[salary-1]

print('The lowest earner is ', person, ': $', minime)
