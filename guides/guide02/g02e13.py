"""
Ingresar la lluvia caída en milímetros para
cada día de la semana. Mostrar al final el
total de lluvia caída y la cantidad de días
que no llovió.
"""
total = 0
didntRain = 0
for i in range(0, 7):
    millimeters = int(input('How many millimeters fell today? Answer: '))
    total = total + millimeters
    if millimeters == 0:
        didntRain = didntRain+1

print('The total number of millimeters that fell this week are', total)
print('The days that did not rain are', didntRain)
