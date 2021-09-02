""" 
Calcular el sueldo a cobrar teniendo en cuenta
que  los empleados que no han faltado y  cuya 
antigüedad es superior a 5 años, tienen un
adicional del 30% sobre el sueldo básico
($47.000). Pedir la cantidad de días 
no trabajados y año de ingreso en la empresa.
"""
daysDidntWork = int(input('Cantidad de días no trabajados: '))
yearsInCompany = int(input('Cantidad de años en la empresa: '))

salary = 47000
additional = 470*30

if daysDidntWork == 0 and yearsInCompany > 5:
    print('Salario a cobrar: $', salary+additional)
else:
    print('Salario a cobrar: $', salary)
