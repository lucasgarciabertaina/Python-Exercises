"""
Dada una serie de números reales positivos,
determinar el valor máximo y mostrarlo al 
final. Se deberá ir preguntando si hay más 
números para ingresar.
"""
question = input('There are numbers to enter? Answer: ')
comparator = 0
while question == 'yes':
    number = float(input('Insert a positive number: '))
    while number <= 0:
        print('The inserted number is less than zero!')
        number = float(input('Insert a positive number: '))
    if number > comparator:
        comparator = number
    question = input('There are numbers to enter? Answer: ')
print('The greater number is: ', comparator)
