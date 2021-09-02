"""
Pedir nombres y sexo de personas y mostrar el
total de mujeres y el nombre de cada una.
"""
condition = input('Wants to continue entering values? Answer: ')
people = []
while condition == 'yes':
    name = input('What is the name? Answer: ')
    genere = input('What is your gender? Answer: ')
    if genere == 'female':
        people.append(name)
    condition = input('Wants to continue entering values? Answer: ')

print('The total is: ', len(people))
for iterator in range(0, len(people)):
    print(people[iterator])
