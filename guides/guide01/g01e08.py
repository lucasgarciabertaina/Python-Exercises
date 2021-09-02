""" 
Pasar un período expresado en segundos a un período expresado
en días, horas, minutos y segundos.
"""
second = int(input('Ingrese la cantidad de segundos: '))

if second / 60 > 0:  # Minutos
    minute = second/60
    minute = int(minute)
    second = second % 60
    if minute / 60 > 0:  # Horas
        hour = minute/60
        hour = int(hour)
        minute = minute % 60
        if hour / 24 > 0:  # Días
            day = hour/24
            day = int(day)
            hour = hour % 24
            print('Días: ', day, ' ', hour, ':', minute, ':', second)
        else:
            print(hour, ':', minute, ':', second)
    else:
        print('0: ', minute, ':', second)
else:
    print('Días 0, 0:0:', second,)
