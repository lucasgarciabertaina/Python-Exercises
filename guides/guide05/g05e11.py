"""
11. Ingresar la lluvia caída en milímetros para
cada día de la semana. Mostrar al final el
total de lluvia caída y el nombre del día que
más llovió.
"""


def weekRain():
    i = 0
    week = []
    while i != 7:
        day = float(input('How many millilitres rain in this day? '))
        week.append(day)
        i += 1
    return week


def dayMostRain(weekRain):
    week = ['Sunday', 'Monday', 'Tueday',
            'Wednesday', 'Thursday', 'Friday', 'Saturday']
    max = 0
    for day in range(len(weekRain)):
        if weekRain[day] > max:
            max = weekRain[day]
            position = day
    return week[position]


print("The day most rain on this week is", dayMostRain(weekRain()))
