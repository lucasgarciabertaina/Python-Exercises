shoes = [
    {'talle': 'S', 'colores': {'rojo': 4, 'verde': 2, 'azul': 0, 'blanco': 1}},
    {'talle': 'M', 'colores': {'rojo': 7, 'verde': 1, 'azul': 3, 'blanco': 7}},
    {'talle': 'L', 'colores': {'rojo': 2, 'verde': 0, 'azul': 4, 'blanco': 4}},
    {'talle': 'XL', 'colores': {'rojo': 3, 'verde': 5, 'azul': 7, 'blanco': 2}},
]

# Obtener:
# Las faltantes, por talle y color.
# El o los colores de remeras de menor cantidad.
# Las remeras con mayor stock, por talle y color.


def faltantes(remeras):
    remeraFaltante = '-Falta la remera de color '
    remerasFaltantes = []
    for remera in remeras:
        talle = remera['talle']
        for color in remera['colores'].keys():
            if remera['colores'][color] == 0:
                remeraFaltante += color
                remeraFaltante += ' talle'
                remeraFaltante += ' '
                remeraFaltante += talle
                remeraFaltante += '.'
                remerasFaltantes.append(remeraFaltante)
                remeraFaltante = '-Falta la remera de color '
    for faltante in remerasFaltantes:
        print(faltante)


def totalColor(remeras):
    totalRojo = 0
    totalVerde = 0
    totalAzul = 0
    totalBlanco = 0
    for remera in remeras:
        for key, value in remera['colores'].items():
            if key == 'rojo':
                totalRojo += value
            elif key == 'verde':
                totalVerde += value
            elif key == 'azul':
                totalAzul += value
            else:
                totalBlanco += value
    cantidadRemeras = ['rojo', totalRojo, 'verde',
                       totalVerde, 'azul', totalAzul, 'blanco', totalBlanco]
    return cantidadRemeras


def menorColor(remeras):
    colores = totalColor(remeras)
    minimo = ''
    iguales = []
    colorMenor = ''
    for i in range(1, len(colores), 2):
        if minimo == '':
            minimo = colores[i]
        elif minimo > colores[i]:
            minimo = colores[i]
            colorMenor = colores[i-1]
            iguales = []
        elif minimo == colores[i]:
            iguales.append(colorMenor)
            iguales.append(colores[i-1])
    if len(iguales) == 0:
        print('El color con menor cantidad es el', colorMenor)
    else:
        print('Los colores con menor cantidad son', iguales)


def mayorCantidad(remeras):
    remeraMayor = []
    maximo = 0
    for remera in remeras:
        talle = remera['talle']
        for color, cantidad in remera['colores'].items():
            if cantidad > maximo:
                maximo = cantidad
                remeraMayor = [talle, color]
            elif cantidad == maximo:
                remeraMayor.append(talle)
                remeraMayor.append(color)
    print('Las remeras de mayor cantidad son: ')
    for i in range(0, len(remeraMayor), 2):
        print('Remera talle', remeraMayor[i], 'color', remeraMayor[i+1])


def main():
    faltantes(shoes)
    menorColor(shoes)
    mayorCantidad(shoes)


if __name__ == '__main__':
    main()
