""" 
Preguntar cuántas personas se van a cargar y 
luego solicitar sus edades, mostrando al 
final la edad promedio.
"""
people = int(input('How many people want to register? Answer: '))
total = 0
for user in range(people):
    age = int(input('How old are you? Answer: '))
    total = total + age
if total <= 0:
    print('No user has entered...')
else:
    average = total/people
    print('The avarage age of ', people, ' people are: ', average, 'years')
