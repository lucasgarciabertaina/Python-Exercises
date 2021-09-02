# Crear dos listas, una de mujeres y otra de varones, cuyos elementos sean diccionarios
# con todos los datos de cada persona, a partir de las siguientes listas paralelas.
# Leer cuidadosamente la consigna!
# A partir de las estructuras de datos obtenidas en el ejercicio anterior, mostrar los nombres de
# las mujeres menores a 55 años y los nombres de los varones más altos que 1.85 metros.
import json
names = ['Khan', 'Omar', 'Sara', 'Ali', 'Mohammed', 'Sofia', 'Mateo']

ages = [60, 50, 55, 70, 25, 20, 40]

heights = [1.75, 1.90, 1.55, 1.80, 1.65, 1.71, 1.88]

sexs = ['M', 'M', 'F', 'M', 'M', 'F', 'M']


def createList(mensAndWommans, mawAges, mawHeights, mawSexs):
    mens = []
    womans = []
    for i in range(7):
        if men(i, sexs):
            mens.append(
                {'name': mensAndWommans[i], 'age': mawAges[i], 'height': mawHeights[i], 'sex': mawSexs[i]})
        else:
            womans.append(
                {'name': mensAndWommans[i], 'age': mawAges[i], 'height': mawHeights[i], 'sex': mawSexs[i]})
    return womans, mens


def men(position, generes):
    if generes[position] == 'M':
        return True
    return False


def firstCondition(females):
    for i in females:
        if i['age'] < 55:
            print(i['name'])


def secondCondition(males):
    for i in males:
        if i['height'] > 1.85:
            print(i['name'])


def main():
    womans, mens = createList(names, ages, heights, sexs)
    jsonStr = json.dumps(womans[0])
    print(womans[1])
    print(jsonStr)
    print(json.loads(jsonStr))
    print(type(jsonStr))
    firstCondition(womans)
    secondCondition(mens)


if __name__ == '__main__':
    main()
