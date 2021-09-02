# 2) Validar un número (reutilizar inputInt/inputFloat
# o bien inputNumber si usan una sola función para
# validar ambos tipos de datos). Debe tener un rango opcional.

def inputController(text):
    while True:
        try:
            value = int(input(text))
            break
        except ValueError:
            print('Please input integer only...')
            continue
    return value


def inputNumber(text, *args, min='', max=''):
    if len(args) == 0 and min == '' and max == '':
        n = inputController(text)
        print(n)
    elif len(args) == 2:
        min = args[0]
        max = args[1]
        n = inputController(text)
        while n > max or n < min:
            n = inputController(
                'The number must be within the assigned range!\n')
        print(n)
    elif max != '' and min == '':
        n = inputController(text)
        while n > max:
            n = inputController('The number is exceeding the maximum!\n')
        print(n)
    elif min != '' and max == '':
        n = inputController(text)
        while min > n:
            n = inputController('The number does not exceed the minimum!\n')
        print(n)
    elif min != '' and max != '':
        n = inputController(text)
        while min > n > max:
            n = inputController(
                'The number must be within the assigned range!\n')
        print(n)


# n = inputNumber('Input a integrer: ', 3, 7)
# m = inputNumber('Any integrer: ')
# maxint = inputNumber('Input a integrer', max=999)
# minint = inputNumber('Input a integrer', min=1001)
