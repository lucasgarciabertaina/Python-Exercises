"""
Ingresar la lluvia caída en milímetros para
cada día de la semana. Mostrar al final el
total de lluvia caída y el nombre del día que
más llovió. (Todos los días llovió distinta
cantidad)
"""
rainDay = 0
total = 0
dayMostRain = ['hello', 0]
week = ['Sunday', 'Monday', 'Tuesday',
        'Wednesday', 'Thursday', 'Friday', 'Saturday']
for day in range(len(week)):
    rainDay = float(input('How many millimeters fell today? Answer: '))
    total = total + rainDay
    if rainDay > dayMostRain[1]:
        dayMostRain = [week[day], rainDay]

print('Total milimiters: ', total)
print('The day of the week that it rained the most was on', dayMostRain[0])
