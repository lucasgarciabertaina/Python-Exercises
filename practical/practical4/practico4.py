"""
Tenemos un archivo deudores.txt con información
de personas que adeudan dinero.

Necesitamos saber el nombre, la dirección de
correo y el saldo de todos los que deben más de
doscientos mil pesos y cuya deuda sea del año
pasado.

Hacer:
Recorrer el archivo deudores.txt y grabar uno
nuevo llamado morosos.txt con los datos
requeridos. 
Para los saldos, el nuevo archivo NO tiene que
tener el signo pesos ($) ni los centavos.
El nuevo archivo tiene que tener cabecera en la
primera línea con los nombres de los datos,
similar al archivo deudores.txt.
"""
from datetime import date


def edad(fn):
    hoy = date.today()
    dn, mn, an = fn.split('/')
    dn = int(dn)
    mn = int(mn)
    an = int(an)
    dh = hoy.day
    mh = hoy.month
    ah = hoy.year
    e = ah - an
    if (mn > mh) or (mn == mh and dn > dh):
        e -= 1
    return e


debtors = open('deudores.txt', 'r').readlines()
defaulingDeb = []
for person in range(1, len(debtors)):
    debtors[person] = debtors[person].split(',')
    debtors[person][4] = float(debtors[person][4][1:])
    if debtors[person][4] > 20000 and edad(debtors[person][5]) == 1:
        defaulingDeb.append([
            debtors[person][1]+', ', debtors[person][2]+', ', str(int(debtors[person][4]))+'\n'])

nonPaying = open('morosos.txt', 'w')
nonPaying.write('nombre, email, saldo.\n')
for line in defaulingDeb:
    nonPaying.writelines(line)
