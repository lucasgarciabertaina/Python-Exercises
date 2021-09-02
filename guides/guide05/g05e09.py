"""
9. Dada una lista cargada con números enteros,
obtener el promedio de ellos. Mostrar por 
pantalla dicho promedio y los números ingresados
que sean mayores que él. Dos funciones:
promedio y mayorQue.
"""


def average(numbers):
    total = 0
    for number in numbers:
        total += number
    return total/len(numbers)


def greaterThan(average, numbers):
    greater = []
    for number in numbers:
        if number > average:
            greater.append(number)
    return greater


print("The average is", average([6, 9, 6]), "and greater than", average(
    [6, 9, 6]), "is/are:", greaterThan(average([6, 9, 6]), [6, 9, 6]))
