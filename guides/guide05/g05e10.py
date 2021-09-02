"""
10. Cargar una lista con números. Invertir los
elementos (sin usar reverse). Mostrar.
"""


def reverse(numbers):
    reverse = []
    for i in range(len(numbers)-1, -1, -1):
        reverse.append(numbers[i])
    print(reverse)
