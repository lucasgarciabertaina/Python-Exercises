"""
Cargar en listas los nombres y fechas de
nacimiento de varias personas, luego recorrerlo
y mostrar los nombres de los mayores de edad.
"""
names = ['Carl', 'Max', 'Paul', 'Chad', 'Bryan', 'Jhon']
bornDays = ['03/04/2004', '08/09/2008', '24/11/1999',
            '26/02/2000', '16/12/1984', '30/01/2009']
year = ''
legalAge = []

for i in range(len(bornDays)):
    for j in range(6, len(bornDays[i])):
        year += bornDays[i][j]
    if int(year) < 2003:
        legalAge.append(names[i])
        year = ''
    else:
        year = ''

print('Persons of legal age are', legalAge)
