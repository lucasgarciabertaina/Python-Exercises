# Dado el archivo de texto practico7.json, obtener:
# 1) Nombres y correos electrónicos de las personas cuyo dominio no sea .com
# 2) La cantidad de personas por país
# 3) El nombre del idioma hablado por la mayor cantidad de personas
from json import loads

jsonRead = open('practico7.json', 'r')
data = loads(jsonRead.read())


def menu(data):
    op = ''
    while op != '4':
        if op == '':
            print('Hi, welcome to practice number 7!')
        print('What exercise do you want to see?')
        print('1) Exercise 1:')
        print('2) Exercise 2:')
        print('3) Exercise 3:')
        print('4) Exit')
        op = input()
        print('=====================')
        if op == '1':
            print('EXERCISE 1')
            for i in data:
                if i['email'][-4:] != '.com':
                    print(i['name'], i['email'])
            print('EXERCISE 1')
            print('=====================')
        elif op == '2':
            print('EXERCISE 2')
            contry = []
            total = []
            for i in data:
                contry.append(i['location']['country'])
            for j in contry:
                if total.count(j) == 0:
                    total.append(j)
                    total.append(1)
                else:
                    total[total.index(j)+1] += 1
            for i in range(0, len(total), 2):
                print(total[i]+': '+str(total[i+1]))
            print('EXERCISE 2')
            print('=====================')
        elif op == '3':
            print('EXERCISE 3')
            total = []
            language = []
            for i in data:
                for j in range(len(i['languages'])):
                    language.append(i['languages'][j])
            for k in language:
                if total.count(k) == 0:
                    total.append(k)
                    total.append(1)
                else:
                    total[total.index(k)+1] += 1
            counter = 0
            languageTalk = ''
            for h in range(1, len(total), 2):
                if total[h] >= counter:
                    counter = total[h]
                    languageTalk = total[h-1]
            print('The lenguage more used is',
                  languageTalk, 'with', counter, 'talkers')
            print('EXERCISE 3')
            print('=====================')


menu(data)
