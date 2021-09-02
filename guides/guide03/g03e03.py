"""
#1: Almacenar en dos listas paralelas,
nombres y sexos de 8 personas.
#2: Recorrerlas y guardar los nombres de las
mujeres en una nueva lista.
#3. Mostrar los elementos de la lista
resultante.
"""
names = ['Carla', 'Pedro', 'Victoria', 'Raul',
         'Candela', 'Camila', 'Lucas', 'Pedro']
genere = ['female', 'male', 'female', 'male',
          'female', 'female', 'male', 'male']

females = []

for i in range(8):
    if genere[i] == 'female':
        females.append(names[i])

print('Women are: ', females)
