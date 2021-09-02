# Se debe realizar el juego MILES.

# Este juego consiste en adivinar un número de 4 cifras que piensa la computadora.
# Dicho número no puede tener cifras repetidas y debe ser superior a 1000 (no puede comenzar con cero).

# El jugador va proponiendo números y el programa le contesta los aciertos:

# Si un dígito del usuario está en el número de la computadora la respuesta será:
# well, si está en la misma posición
# regular si está presente pero en otra posición
# keep trying si no está

# Se termina al adivinar el número exacto y se debe almacenar en un archivo de
# texto el nombre del jugador y la cantidad de intentos que le llevó ganar.

# El programa también debe permitir mostrar el top ten del ranking de jugadores,
# ordenados por las sesiones con menor cantidad de intentos para el acierto.
from random import randint
from typing import Text


def inputOptions(text):
    array = text.split('(')
    word = ''
    options = []
    inp = input(text)
    for i in range(len(array[1])):
        if array[1][i] == '/' or array[1][i] == ')':
            options.append(word)
            word = ''
        else:
            word += array[1][i]
    for i in options:
        if i == inp:
            return i
    return inputOptions("This option doesn't exist. Please write one of the follow options.\n"+text)


def dontRepited(number):
    for i in number:
        if number.count(i) != 1:
            return True
    return False


def inputNumber(text, min=1000, max=9999):
    number = int(input(text))
    while number < min or number > max:
        print('You must enter a number between 1000 and 9999!')
        number = input(text)
    return str(number)


def pcAnswer(nUser, nPc):
    same = 0
    similar = 0
    for i in range(4):
        if nUser[i] == nPc[i]:
            same += 1
    for i in nPc:
        if i == nUser[0] and nPc.index(i) != 0:
            similar += 1
        elif i == nUser[1] and nPc.index(i) != 1:
            similar += 1
        elif i == nUser[2] and nPc.index(i) != 2:
            similar += 1
        elif i == nUser[3] and nPc.index(i) != 3:
            similar += 1
    if same != 0 and same != 4:
        return True, 'But well'
    elif similar != 0:
        return True, 'But regular'
    elif same == 4:
        return False, 'You Won!'
    else:
        return True, 'But keep trying'


def score(line):
    line = line.split(',')
    line[1] = line[1].split(' ')
    return line[1][0]


def nickname(line):
    line = line.split(',')
    return line[0][3:]


def takeAll(lin):
    array = lin[1:]
    allin = []
    counter = 0
    for i in array:
        if i != '------------------\n':
            allin.append(i)
        else:
            counter += 1
    return allin, counter


def insertScore(lins, sc, nn):
    completeScore, count = takeAll(lins)
    scores = {}
    attempts = []
    for line in completeScore:
        attempts.append(int(score(line)))
        scores[score(line)] = nickname(line)
    scores[sc] = nn
    attempts.append(int(sc))
    attempts.sort()
    result = ['Name,Score\n']
    text = ''
    for i in range(len(attempts)):
        text = str(i+1)+') '+scores[str(attempts[i])] + \
            ','+str(attempts[i])+' attemps\n'
        result.append(text)
        text = ''
    if count == 0:
        result.pop()
    elif count == 1:
        return result
    elif count > 1:
        for i in range(count-1):
            result.append('------------------\n')
    return result


option = inputOptions('Do you want to play? (yes/no)\n')
if option == 'yes':
    numberPc = str(randint(1001, 9999))
    while dontRepited(numberPc):
        numberPc = str(randint(1001, 9999))
    print('Answer: ', numberPc)
    numberUser = inputNumber('Enter a number of 4 digits:  ')
    answer = pcAnswer(numberUser, numberPc)
    attempts = 1
    while answer[0]:
        print('Incorrect.', answer[1])
        numberUser = inputNumber('Enter a number of 4 digits:  ')
        attempts += 1
        answer = pcAnswer(numberUser, numberPc)
    print(answer[1])
    nick = input('Please insert you nickname\n')
    readScore = open('score.txt', 'r')

    lines = readScore.readlines()
    results = insertScore(lines, str(attempts), nick)

    writeScores = open('score.txt', 'w')
    writeScores.writelines(results)
