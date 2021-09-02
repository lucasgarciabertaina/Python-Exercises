""" 
El costo del pasaje a Córdoba es de $1700.
La empresa realiza un descuento de un 40 % 
sobre el costo del boleto a los niños que tienen
entre 5 y 10 años y a los jubilados
(mayores de 65). Pedir nombre y edad y
mostrar el nombre y el valor final del pasaje.
"""
name = input('Nombre: ')
age = int(input('Edad: '))
cost = 1700
discont = 40*17

if age > 4 and age < 11:
    print(name, ' le corresponde pagar $', cost-discont)
elif age > 65:
    print(name, ' le corresponde pagar $', cost-discont)
else:
    print(name, ' le corresponde pagar $', cost)
