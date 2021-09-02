# Realizar una aplicación para Alquiler de Cabañas.
# Los datos se obtienen y se almacenan en el archivo separado por comas cabins.csv
# En una primera etapa, NO trabajaremos las fechas, solamente si está o no ocupada el día
# en curso.
# Las opciones de menú deben ser:
# 1- Mostrar todas las cabañas con todos sus datos
# 2- Consultar disponibles por cantidad de pasajeros
# 3- Consultar por rango de precios
from datetime import *


def readProps():
    readProps = open('cabins.csv', 'r')
    array = readProps.readlines()
    props = []
    for i in array:
        if array.index(i) != 0:
            props.append(i[0:-1])
        elif array.index(i) != 0:
            props.append(i)
    return props


def showCabins():
    props = readProps()
    for i in props:
        showCabin(i)


def showCabin(prop):
    propArray = prop.split(',')
    print('====Cabin number', str(propArray[0]), '====')
    print('Number of passengers:', str(propArray[1]))
    print('Price:', str(propArray[2]))
    print('Reserved:', str(propArray[3]))
    print('In:', str(propArray[4]))
    print('Out:', str(propArray[5]), '\n')


def pasagersCabins(number):
    props = readProps()
    cabins = []
    for i in props:
        if number == int(i.split(',')[1]):
            cabins.append(i.split(',')[0])
    return cabins


def avaliableTickets():
    quantity = int(input('Please insert number of passengers:\n'))
    totalCabins = pasagersCabins(quantity)
    cabinsArray = avariable(totalCabins)
    if len(cabinsArray) != 0:
        cabins = '('
        for i in cabinsArray:
            print('- Cabin number', str(i))
            if cabinsArray.index(i) == len(cabinsArray)-1:
                cabins += i
                cabins += ')'
            else:
                cabins += i
                cabins += '/'
        option = inputOptions(cabins)
        bookCabin(option)
    else:
        print('no', quantity, '-person cabins available')


def prices():
    props = readProps()
    prices = []
    for i in props:
        prices.append(int(i.split(',')[2][1:]))
    return prices


def chabinRange(money, allPrices):
    positions = []
    for i in range(len(allPrices)):
        if allPrices[i] <= money:
            positions.append(i)
    return positions


def priciesRange():
    disponibility = int(input('Up to how much you are willing to pay?\n$'))
    cabinsPrices = prices()
    cabinsRange = chabinRange(disponibility, cabinsPrices)
    cabins = ''
    if len(cabinsRange) != 0:
        cabinsPosition = avariable(cabinsRange)
        cabins += '('
        if len(cabinsPosition) != 0:
            for i in cabinsPosition:
                cabins += str(i)
                if cabinsRange.index(i) != len(cabinsRange)-1:
                    cabins += '/'
                else:
                    cabins += ')'
            print('There is/are avariable the cabin/s number', cabins)
            option = inputOptions(cabins)
            bookCabin(option)
        else:
            print('There are no cabins available at', disponibility, 'pesos.')
    else:
        print('There are no cabins available at', disponibility, 'pesos.')


def avariable(numberCabins):
    props = readProps()
    cabins = []
    for i in props:
        for j in numberCabins:
            if int(j) == int(i.split(',')[0]):
                if i.split(',')[3] == 'no':
                    cabins.append(j)
    return cabins


def bookCabin(cabin):
    props = readProps()
    newProps = []
    propStr = ''
    for i in range(len(props)):
        if props[i].split(',')[0] == cabin:
            propBook = props[i].split(',')
            propBook[3] = 'si'
            dateToday = date.today()
            today = datetime.strftime(dateToday, '%d/%m/%Y')
            propBook[4] = str(today)
            for k in range(5):
                if k == 4:
                    propStr += propBook[k]
                    propStr += ',\n'
                else:
                    propStr += propBook[k]
                    propStr += ','
    for l in range(len(props)+1):
        if l == 0:
            newProps.append('Número,Pasajeros,Precio,Reservada,In,Out\n')
        elif props[l-1].split(',')[0] == cabin:
            newProps.append(propStr)
        else:
            props[l-1] += '\n'
            newProps.append(props[l-1])
    newCabins = open('cabins.csv', 'w')
    newCabins.writelines(newProps)


def inputOptions(strOptions):
    arrayOptions = strOptions.split('(')
    word = ''
    options = []
    inp = input()
    for i in range(len(arrayOptions[1])):
        if arrayOptions[1][i] == '/' or arrayOptions[1][i] == ')':
            options.append(word)
            word = ''
        else:
            word += arrayOptions[1][i]
    for i in options:
        if i == inp:
            return i
    return inputOptions("This option doesn't exist. Please write one of the follow options.\n"+strOptions)


def menu(**kwargs):
    counter = 1
    print('=====MENU====\n')
    keys = ['hi']
    options = '('
    for key, value in kwargs.items():
        print(counter, ')', value)
        options += str(counter)
        options += '/'
        counter += 1
        keys.append(key)
    print(len(kwargs)+1, ') Close menú')
    options += str(counter)
    options += ')'
    option = inputOptions(options)
    for k in range(len(keys)):
        if str(k) == option:
            eval(keys[k]+'()')
            return menu(**kwargs)


def main():
    menu(showCabins='Show Cabins', avaliableTickets='Availability by number of tickets',
         priciesRange='Consult by price range')
    readProps()


if __name__ == '__main__':
    main()
