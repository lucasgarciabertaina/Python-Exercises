# 6) input de fechas (validar formato y devolver año, mes y día como enteros),
#  debe forzar un formato estricto, por ejemplo dd/mm/aaaa.


def inputDate(text):
    date = input(text)
    while comprobatorDate(date):
        date = input(
            'This date is incorrect. Please try again (dd/mm/yyy)\n'+text)
    print('Today is ', date)


def comprobatorDate(d):
    if len(d) != 10:
        return True
    for i in range(len(d)):
        print(i, d[i])
        if i == 2 or i == 5:
            if d[i] != '/':
                print('hi')
                return True
        else:
            if not d[i].isnumeric():
                return True
    return False


# print(len('02/04/2016'))
# inputDate('What date is today?\n')
