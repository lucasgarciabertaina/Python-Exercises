# Realizar una aplicación que maneje una Lista de Tareas.
# Deben decidir que categorías utilizar (ej: trabajo, estudio, personal, etc.), el manejo del
# tiempo (fechas, urgencias, límites temporales, etc.)
# También deben decidir que estructuras de datos usar, listas y/o diccionarios y/o archivos de texto, etc.
# Agregar la mayor cantidad de variantes útiles posible!


# Es obligatorio implementar el práctico con la estructura trabajada en la clase del
#  3 de agosto (ver comentarios en las Novedades)
from datetime import *


def readProps():
    readProps = open('tasks.txt', 'r')
    array = readProps.readlines()
    props = []
    for i in array:
        if i[-1] == '\n' and array.index(i) != 0:
            props.append(i[0:-1])
        elif array.index(i) != 0:
            props.append(i)
    return props


def taskDate(prop):
    elements = prop.split(',')
    return elements[1]


def task(prop):
    elements = prop.split(',')
    return elements[0]


def taskType(prop):
    elements = prop.split(',')
    return elements[2]


def tasksToday():
    props = readProps()
    todayDateTime = datetime.now()
    today = datetime.strftime(todayDateTime, '%d/%m/%Y')
    tasks = []
    for i in props:
        if taskDate(i) == today:
            tasks.append(task(i))
    print('Tasks for today:\n')
    for j in tasks:
        print('-', j)


def tasksTomorrow():
    props = readProps()
    tomorrowDateTime = datetime.now() + timedelta(days=1)
    tomorrow = datetime.strftime(tomorrowDateTime, '%d/%m/%Y')
    tasks = []
    for i in props:
        if taskDate(i) == tomorrow:
            tasks.append(task(i))
    print('Tasks for tomorrow:\n')
    for j in tasks:
        print('-', j)


def insertTask():
    prop = ''
    prop += input('Insert a task:\n')
    prop += ','
    prop += input('Insert the date (dd/mm/yyyy):\n')
    prop += ','
    prop += input('What type is the task (personal/office)\n')
    prop += ','
    prop += str(False)
    prop += '\n'
    writeFile = open('tasks.txt', 'a')
    writeFile.write(prop)


def dayDifference(day, anotherDay):
    differenceArray = str(date(int(day[6:]), int(day[3:5]), int(day[0:2])) - date(
        int(anotherDay[6:]), int(anotherDay[3:5]), int(anotherDay[0:2]))).split(' ')
    numberDifference = differenceArray[0]
    if len(differenceArray) < 3:
        return -1, True
    if numberDifference[0] == '-':
        return int(numberDifference[1:]), False
    return int(numberDifference), True


def missingTasks():
    props = readProps()
    todayDateTime = datetime.now()
    today = datetime.strftime(todayDateTime, '%d/%m/%Y')
    tasks = []
    for i in props:
        differrence, condition = dayDifference(taskDate(i), today)
        if differrence >= 0 and condition and props[3] != False:
            tasks.append(task(i))
        elif differrence == -1 and condition:
            tasks.append(task(i))
    print('Missing tasks:\n')
    for j in tasks:
        print('-', j)


def officeTask():
    props = readProps()
    tasks = []
    for i in props:
        if taskType(i) == 'office':
            tasks.append(task(i))
    print('Office tasks :\n')
    for j in tasks:
        print('-', j)


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
    #    menu(insertTask='Add tasks', tasksToday='Tasks for today',tasksTomorrow='Tasks for tomorrow', missingTasks='Missing Tasks', officeTask='Office tasks')
    diccionario = {'vaca': 24, 2: 'c', 'estaBien': 'values'}
    # for key in diccionario.keys():
    #    print(key)
    # for value in diccionario.values():
    #    print(value)
    # for key, value in diccionario.items():
    #    print(key, value)


if __name__ == '__main__':
    main()
