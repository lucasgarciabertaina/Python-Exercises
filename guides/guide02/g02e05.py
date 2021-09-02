"""
Pedir los montos de sueldos de los empleados de
una empresa hasta que no haya más y mostrar
el total.
"""
askForAmounts = input('Do you have a deposit amount? ')
total = 0
while askForAmounts != 'No':
    amount = float(input('Enter the amount: '))
    total = total + amount
    askForAmounts = input('Do you have a deposit amount? ')
print('Your total is: $', total)
